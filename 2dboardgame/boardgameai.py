import numpy as np
import random
import sys
import time
import copy

# Set recursion limit higher for MCTS
sys.setrecursionlimit(4000)

# --- CONFIGURATION ---
BOARD_WIDTH = 19
INPUT_CHANNELS = 2  # Player 1 stones, Player 2 stones
INPUT_SIZE = BOARD_WIDTH * BOARD_WIDTH * INPUT_CHANNELS
HIDDEN_SIZE = 1024
POLICY_OUTPUT_SIZE = BOARD_WIDTH * BOARD_WIDTH  # 19*19 = 361 moves
VALUE_OUTPUT_SIZE = 1  # Game outcome prediction
LEARNING_RATE = 0.0001
GENERATIONS_SELF_PLAY = 5000  # Total training games increased to 5000

# MCTS Parameters
C_PUCT = 1.0  # Exploration constant in UCB formula
NUM_SIMULATIONS = 200  # Number of MCTS simulations per move (lower for speed)
TEMPERATURE = 1.0  # Controls policy randomness in training

# Delays
TRAINING_DELAY_SECONDS = 0.001
PLAY_DELAY_SECONDS = 2.0


# --- HELPER FUNCTIONS (Activation Functions) ---
def relu(x):
    return np.maximum(0, x)


def relu_derivative(x):
    return (x > 0).astype(float)


def tanh(x):
    return np.tanh(x)


def tanh_derivative(x):
    return 1.0 - x ** 2


def softmax(x):
    """Numerically stable softmax for policy head."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=1, keepdims=True)


# --- OPTIMIZER ---
class AdamOptimizer:
    def __init__(self, learning_rate=LEARNING_RATE, beta1=0.9, beta2=0.999, epsilon=1e-8):
        self.learning_rate = learning_rate
        self.beta1 = beta1;
        self.beta2 = beta2;
        self.epsilon = epsilon
        self.m = {};
        self.v = {};
        self.t = 0

    def update(self, weights_key, gradient):
        self.t += 1
        if weights_key not in self.m:
            self.m[weights_key] = np.zeros_like(gradient)
            self.v[weights_key] = np.zeros_like(gradient)
        self.m[weights_key] = self.beta1 * self.m[weights_key] + (1 - self.beta1) * gradient
        self.v[weights_key] = self.beta2 * self.v[weights_key] + (1 - self.beta2) * (gradient ** 2)
        m_hat = self.m[weights_key] / (1 - self.beta1 ** self.t)
        v_hat = self.v[weights_key] / (1 - self.beta2 ** self.t)
        update_step = self.learning_rate * m_hat / (np.sqrt(v_hat) + self.epsilon)
        return update_step


# --- NEURAL NETWORK (POLICY/VALUE) ---
class PolicyValueNN:
    def __init__(self, input_size, hidden_size, policy_size, value_size, optimizer):
        self.optimizer = optimizer

        # Shared Hidden Layer Weights (Deep FFN)
        self.W1 = np.random.randn(input_size, hidden_size) * np.sqrt(2 / input_size);
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, hidden_size) * np.sqrt(2 / hidden_size);
        self.b2 = np.zeros((1, hidden_size))

        # Policy Head Weights
        self.Wp = np.random.randn(hidden_size, policy_size) * np.sqrt(2 / hidden_size);
        self.bp = np.zeros((1, policy_size))

        # Value Head Weights
        self.Wv = np.random.randn(hidden_size, value_size) * np.sqrt(2 / hidden_size);
        self.bv = np.zeros((1, value_size))

        # Storage for forward pass outputs
        self.h1_out = None;
        self.h2_out = None
        self.policy_logits = None;
        self.value_out = None

    def _prepare_input(self, board):
        """Converts board state into a 1D input vector with two channels (P1, P2)."""
        input_vector = []
        for r in range(BOARD_WIDTH):
            for c in range(BOARD_WIDTH):
                is_p1 = 1 if board[r][c] == 1 else 0
                is_p2 = 1 if board[r][c] == 2 else 0
                input_vector.extend([is_p1, is_p2])
        return np.array(input_vector).reshape(1, -1)

    def forward(self, board):
        X = self._prepare_input(board)

        # Shared FFN Layers (ReLU)
        z1 = np.dot(X, self.W1) + self.b1;
        self.h1_out = relu(z1)
        z2 = np.dot(self.h1_out, self.W2) + self.b2;
        self.h2_out = relu(z2)

        # Policy Head (Logits for Softmax)
        self.policy_logits = np.dot(self.h2_out, self.Wp) + self.bp
        policy_probs = softmax(self.policy_logits)

        # Value Head (Tanh for output in [-1, 1])
        z_v = np.dot(self.h2_out, self.Wv) + self.bv
        self.value_out = tanh(z_v)

        return policy_probs, self.value_out

    def backprop(self, board, target_policy, target_value):
        X = self._prepare_input(board)

        # --- Forward Pass (Need to re-run to get all internal values) ---
        z1 = np.dot(X, self.W1) + self.b1;
        h1 = relu(z1)
        z2 = np.dot(h1, self.W2) + self.b2;
        h2 = relu(z2)
        policy_logits = np.dot(h2, self.Wp) + self.bp
        policy_probs = softmax(policy_logits)
        z_v = np.dot(h2, self.Wv) + self.bv
        value_out = tanh(z_v)

        # --- Backprop (Combined Loss) ---

        # 1. Value Head Gradients (MSE Loss)
        d_value = 2 * (value_out - target_value)  # Loss is (v - z)^2
        d_z_v = d_value * tanh_derivative(value_out)
        d_Wv = np.dot(h2.T, d_z_v);
        d_bv = np.sum(d_z_v, axis=0, keepdims=True)

        # 2. Policy Head Gradients (Cross-Entropy Loss)
        # dL/dWp = (policy_probs - target_policy) * h2.T (Simplified for Softmax/Cross-Entropy)
        d_policy = policy_probs - target_policy
        d_Wp = np.dot(h2.T, d_policy);
        d_bp = np.sum(d_policy, axis=0, keepdims=True)

        # 3. Shared Layer Gradients (Sum of policy and value contributions)
        d_h2_from_value = np.dot(d_z_v, self.Wv.T)
        d_h2_from_policy = np.dot(d_policy, self.Wp.T)
        d_h2 = d_h2_from_value + d_h2_from_policy

        d_z2 = d_h2 * relu_derivative(h2)
        d_W2 = np.dot(h1.T, d_z2);
        d_b2 = np.sum(d_z2, axis=0, keepdims=True)
        d_h1 = np.dot(d_z2, self.W2.T)

        d_z1 = d_h1 * relu_derivative(h1)
        d_W1 = np.dot(X.T, d_z1);
        d_b1 = np.sum(d_z1, axis=0, keepdims=True)

        # --- Update Weights (Adam) ---
        self.Wv -= self.optimizer.update('Wv', d_Wv);
        self.bv -= self.optimizer.update('bv', d_bv)
        self.Wp -= self.optimizer.update('Wp', d_Wp);
        self.bp -= self.optimizer.update('bp', d_bp)
        self.W2 -= self.optimizer.update('W2', d_W2);
        self.b2 -= self.optimizer.update('b2', d_b2)
        self.W1 -= self.optimizer.update('W1', d_W1);
        self.b1 -= self.optimizer.update('b1', d_b1)


# --- MCTS NODE AND SEARCH ---

class MCTSNode:
    def __init__(self, parent, move, prior_prob, move_player):
        self.parent = parent
        self.move = move
        self.prior_prob = prior_prob
        self.children = {}  # (r, c) -> MCTSNode
        self.visit_count = 0
        self.total_action_value = 0.0  # W
        self.move_player = move_player  # The player who made the move (r,c) to reach this node's state

    def is_leaf(self):
        return self.children == {}

    def value(self):
        return self.total_action_value / self.visit_count if self.visit_count > 0 else 0.0


class MCTS:
    def __init__(self, nn_model, board_ref, current_generation):
        self.nn_model = nn_model
        self.board_ref = board_ref
        self.current_generation = current_generation

    def run_simulation(self, root_node, board_state, player_turn):
        # 1. Selection
        node = root_node
        path = [node]
        current_board = copy.deepcopy(board_state)
        current_player = player_turn

        # Traverse the tree until a leaf node is reached
        while not node.is_leaf():
            r, c, node = self._select_child(node, current_player)
            # Make the move on the temporary board
            Board.static_make_move(current_board, r, c, current_player)
            current_player = 3 - current_player
            path.append(node)

        # Check for immediate win/draw at the leaf node state
        winner = self.board_ref.static_check_winner(current_board)
        if winner is not None:
            # Value is determined from the perspective of the player *whose turn it is* at the leaf.
            value = 0.0 if winner == 0 else (1.0 if winner == current_player else -1.0)
        else:
            # 2. Expansion and Evaluation (for non-terminal leaf)
            policy_probs, value_prediction = self.nn_model.forward(current_board)
            value = value_prediction[0][0]  # Estimated value from NN [-1, 1]

            # Expansion
            self._expand_node(node, policy_probs, current_board, current_player)

        # 3. Backpropagation
        self._backpropagate(path, value)

    def _select_child(self, node, player):
        best_ucb = -float('inf')
        best_move = None
        best_child = None

        for move, child in node.children.items():
            # Upper Confidence Bound (UCB) calculation: Q + U
            # Q value is stored as the expected outcome for the player who made the move to reach the child node
            # We need to adjust it to the current player's perspective for selection.
            Q = child.value() * (1 if child.move_player == player else -1)
            U = C_PUCT * child.prior_prob * np.sqrt(node.visit_count) / (1 + child.visit_count)
            ucb = Q + U

            if ucb > best_ucb:
                best_ucb = ucb
                best_move = move
                best_child = child

        return best_move[0], best_move[1], best_child

    def _expand_node(self, node, policy_probs, current_board, player_to_move):

        # MASK LOGIC: Mask for empty spots
        mask = np.array([1 if current_board[r][c] == 0 else 0
                         for r in range(BOARD_WIDTH) for c in range(BOARD_WIDTH)])

        # Apply mask and re-normalize probabilities
        valid_probs = policy_probs * mask
        sum_valid = np.sum(valid_probs)
        if sum_valid > 0:
            valid_probs /= sum_valid

        for i, prob in enumerate(valid_probs[0]):
            if prob > 0:
                r, c = divmod(i, BOARD_WIDTH)
                # The move (r, c) will be made by `player_to_move`
                node.children[(r, c)] = MCTSNode(node, (r, c), prob, player_to_move)

    def _backpropagate(self, path, value):
        """Propagates the final outcome (value) up the MCTS tree, flipping the perspective at each level."""
        for node in reversed(path):
            node.visit_count += 1
            node.total_action_value += value  # The value is relative to the player who made the move to reach this state
            value *= -1  # Flip the value for the parent node (opponent's perspective)

    def get_move_and_policy(self, board_state, player_turn):
        root = MCTSNode(None, None, 0.0, None)

        # Initial expansion of the root
        policy_probs, _ = self.nn_model.forward(board_state)
        # The player to move from the root is `player_turn`
        self._expand_node(root, policy_probs, board_state, player_turn)

        for _ in range(NUM_SIMULATIONS):
            self.run_simulation(root, board_state, player_turn)

        # Policy target generation (Normalized visit counts)
        policy_target = np.zeros(POLICY_OUTPUT_SIZE)

        # Get move based on visit counts raised to a temperature power
        move_visits = {move: child.visit_count for move, child in root.children.items()}

        # Handle the case where MCTS couldn't find any move (shouldn't happen on non-terminal board)
        if not move_visits:
            # Fallback for a full board or error
            return (-1, -1), policy_target.reshape(1, -1), 0.0

        # Apply temperature for exploration during training, or choose deterministically in play
        moves, visits = zip(*move_visits.items())

        if self.current_generation is not None:
            # Training: Use temperature
            visits_temp = np.array(visits) ** (1.0 / TEMPERATURE)
            probs = visits_temp / np.sum(visits_temp)

            # Create policy target vector (for training)
            for i, move in enumerate(moves):
                idx = move[0] * BOARD_WIDTH + move[1]
                policy_target[idx] = visits[i] / root.visit_count

            # Select move based on probabilities
            move_index = np.random.choice(range(len(moves)), p=probs)
            r, c = moves[move_index]

            # Confidence metric (probability of the chosen move)
            confidence = probs[move_index] * 100
        else:
            # Final Play: Choose move with max visit count
            max_visits = max(visits)
            best_moves = [move for move, visit in move_visits.items() if visit == max_visits]
            r, c = random.choice(best_moves)

            # Confidence metric
            confidence = max_visits / root.visit_count * 100

        return (r, c), policy_target.reshape(1, -1), confidence


# --- BOARD CLASS ---
class Board:
    def __init__(self, width, delay_seconds, current_generation=None):
        self.width = width
        self.board = [[0] * width for _ in range(width)]
        self.player_turn = 1
        self.row = -1;
        self.column = -1
        self.moves_history = [];
        self.turn_count = 0;
        self.game_over = False
        self.delay = delay_seconds
        self.generation = current_generation  # Store generation
        self.policy_value_nn = None
        self.total_confidence = 0.0

    @staticmethod
    def static_make_move(board, r, c, player):
        """Used internally by MCTS for temporary board updates."""
        board[r][c] = player

    @staticmethod
    def static_check_winner(board):
        """Checks for a winner in a static board state. Returns player (1/2), 0 for draw, or None."""
        width = len(board)
        # Check for full board (Draw)
        if all(board[r][c] != 0 for r in range(width) for c in range(width)):
            return 0  # Draw

        # Check for 5-in-a-row
        for r in range(width):
            for c in range(width):
                player = board[r][c]
                if player != 0:
                    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
                    for dr, dc in directions:
                        for start in range(-4, 1):
                            count = 0
                            for i in range(5):
                                nr, nc = r + (start + i) * dr, c + (start + i) * dc
                                if 0 <= nr < width and 0 <= nc < width and board[nr][nc] == player:
                                    count += 1
                                else:
                                    break
                            if count == 5:
                                return player
        return None

    def check_game_over(self):
        self.winner = self.static_check_winner(self.board)
        if self.winner is not None:
            self.game_over = True
            return True
        return False

    def is_adjacent_to_existing(self, r, c):
        """Checks if a spot (r, c) is adjacent (including diagonal) to an existing piece."""
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.width and 0 <= nc < self.width and self.board[nr][nc] != 0:
                return True
        return False

    def get_incremental_penalty(self, r, c, player):
        """Returns 0.0 as the adjacency rule is now strictly enforced by move selection."""
        return 0.0

    def print_board(self, show_progress=True):
        if show_progress:
            print("Current Board:");
            col_indices = "   " + " ".join([f"{c:2d}" for c in range(self.width)])
            print(col_indices);
            print("  " + "-" * (self.width * 3 + 1))
            for k in range(self.width):
                printable = f"{k:2d}| ";
                for y in self.board[k]:
                    if y == 1:
                        y_str = "\033[91m1\033[0m"
                    elif y == 2:
                        y_str = "\033[92m2\033[0m"
                    else:
                        y_str = "0"
                    printable += y_str + '  '
                print(printable)
            print("-" * (self.width * 3 + 4))
            time.sleep(self.delay)

    def make_move(self, r, c, player_num, policy_target=None, confidence=None, show_progress=True):
        if not (0 <= r < self.width and 0 <= c < self.width) or self.board[r][c] != 0:
            return False, "Invalid move."

        # Penalty is 0.0 due to strict enforcement logic in ai_turn
        penalty = self.get_incremental_penalty(r, c, player_num)

        # Store data for MCTS-based training later
        self.moves_history.append({
            'state': copy.deepcopy(self.board),
            'player': player_num,
            'policy': policy_target,
            'penalty': penalty,
            'confidence': confidence
        })

        if confidence is not None and policy_target is not None:
            self.total_confidence += confidence

        self.row = r;
        self.column = c;
        self.board[r][c] = player_num
        self.turn_count += 1

        self.check_game_over()

        if not self.game_over: self.player_turn = 3 - self.player_turn

        if show_progress:
            self.print_board(show_progress)

        return True, "Move successful."

    def human_turn(self):
        while True:
            try:
                r = int(input(f"Player {self.player_turn} (Human P1), enter row (0-{self.width - 1}): "))
                c = int(input(f"Player {self.player_turn} (Human P1), enter column (0-{self.width - 1}): "))

                # Check for adjacency rule enforcement for the human player
                if self.turn_count > 0 and not self.is_adjacent_to_existing(r, c):
                    print("🚫 Rule Violation: You must play next to an existing piece. Try again.")
                    continue

                success, message = self.make_move(r, c, self.player_turn, show_progress=True)
                if success:
                    break
                else:
                    print(f"Invalid move: {message}")
            except ValueError:
                print(f"Please enter valid integers (0-{self.width - 1}).")

    def ai_turn(self, ai_model, player_num, current_generation=None):
        mcts = MCTS(ai_model, self, current_generation)

        # Get MCTS result: (r, c), policy_target_vector, confidence
        (r, c), policy_target, confidence = mcts.get_move_and_policy(self.board, player_num)

        if r == -1:  # Board is full or MCTS failed to find a move
            self.game_over = True;
            self.winner = 0
            return

        # --- PERMANENT ADJACENCY ENFORCEMENT ---
        # If it's not the very first move of the game, enforce adjacency.
        if self.turn_count > 0:
            if not self.is_adjacent_to_existing(r, c):
                # Fall back to a random legal ADJACENT move
                empty_spots = [(r_s, c_s) for r_s in range(self.width) for c_s in range(self.width) if
                               self.board[r_s][c_s] == 0]
                adjacent_spots = [(r_s, c_s) for r_s, c_s in empty_spots if self.is_adjacent_to_existing(r_s, c_s)]

                if adjacent_spots:
                    # Override MCTS move with a random legal adjacent move
                    r, c = random.choice(adjacent_spots)
                # If adjacent_spots is empty, something is wrong, but we must proceed.

        self.make_move(r, c, player_num, policy_target, confidence, show_progress=(current_generation is None))


# --- TRAINING FUNCTION (AI VS AI SELF-PLAY) ---

def train_ai_self_play(ai_model, width):
    print("=" * 60)
    print(f"🧠 STARTING MCTS SELF-PLAY TRAINING | {GENERATIONS_SELF_PLAY} Games")
    print(f"  Network: Deep FFN with Policy/Value Heads.")
    print(f"  MCTS Simulations per Move: {NUM_SIMULATIONS}")
    print(f"  RULE: All moves (after the first) must be ADJACENT to an existing piece.")
    print("=" * 60)

    optimizer_self = AdamOptimizer(learning_rate=LEARNING_RATE)
    # The opponent is a separate instance of the NN (older version of P1)
    ai_opponent = PolicyValueNN(INPUT_SIZE, HIDDEN_SIZE, POLICY_OUTPUT_SIZE, VALUE_OUTPUT_SIZE, optimizer_self)

    stats = {'wins_p1': 0, 'wins_p2': 0, 'draws': 0}

    for gen in range(1, GENERATIONS_SELF_PLAY + 1):

        # Reset the opponent model periodically (e.g., every 50 games)
        if gen % 50 == 0:
            ai_opponent.W1 = copy.deepcopy(ai_model.W1);
            ai_opponent.b1 = copy.deepcopy(ai_model.b1)
            ai_opponent.W2 = copy.deepcopy(ai_model.W2);
            ai_opponent.b2 = copy.deepcopy(ai_model.b2)
            ai_opponent.Wp = copy.deepcopy(ai_model.Wp);
            ai_opponent.bp = copy.deepcopy(ai_model.bp)
            ai_opponent.Wv = copy.deepcopy(ai_model.Wv);
            ai_opponent.bv = copy.deepcopy(ai_model.bv)

        # P1 is the model being trained, P2 is the opponent model
        p1_model = ai_model
        p2_model = ai_opponent
        p1_num = 1;
        p2_num = 2

        b = Board(width, delay_seconds=TRAINING_DELAY_SECONDS, current_generation=gen)

        while not b.game_over:
            current_player = b.player_turn
            model = p1_model if current_player == 1 else p2_model

            b.ai_turn(model, current_player, current_generation=gen)

            if b.game_over: break

        # Determine terminal rewards (Value Target: 1 for Win, 0 for Draw, -1 for Loss)
        value_target = 0.0  # Default for Draw
        if b.winner == p1_num:
            value_target = 1.0; stats['wins_p1'] += 1
        elif b.winner == p2_num:
            value_target = -1.0; stats['wins_p2'] += 1
        else:
            stats['draws'] += 1

        # Calculate average confidence metric
        avg_confidence = b.total_confidence / b.turn_count if b.turn_count > 0 else 0.0

        # --- Training Step: Backpropagate all stored states for the game ---
        for move_data in b.moves_history:
            board_state = move_data['state']
            player_moved = move_data['player']
            policy_target = move_data['policy']
            penalty = move_data['penalty']  # penalty is always 0.0 now

            if policy_target is None: continue

            # Value is relative to P1. If P2 made the move, flip the game outcome.
            final_move_value = value_target * (1 if player_moved == p1_num else -1)

            # Add penalty (which is 0.0)
            final_move_value += penalty / 100.0

            # Only train the primary AI (P1)
            if player_moved == p1_num:
                p1_model.backprop(board_state, policy_target, np.array([[final_move_value]]))

        if gen % 10 == 0:
            print(
                f"| Gen {gen:4d}/{GENERATIONS_SELF_PLAY} | P1 Wins: {stats['wins_p1']:4d} | P2 Wins: {stats['wins_p2']:4d} | Draws: {stats['draws']:4d} | Avg. Confidence: {avg_confidence:.2f}% |")

    print(f"\n✅ TRAINING COMPLETE: AI finished {GENERATIONS_SELF_PLAY} self-play games.")
    return ai_model


# 1. Initialize AI Models and Optimizer
optimizer = AdamOptimizer()
neural_net_ai = PolicyValueNN(INPUT_SIZE, HIDDEN_SIZE, POLICY_OUTPUT_SIZE, VALUE_OUTPUT_SIZE, optimizer)

# 2. Start Self-Play Training (Phase 1)
trained_ai = train_ai_self_play(neural_net_ai, BOARD_WIDTH)

# 3. Final 1v1 against the User (Phase 2)
play_game(BOARD_WIDTH, trained_ai)
