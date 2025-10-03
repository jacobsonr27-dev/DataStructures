class Board:
    def __init__(self, width):
        self.board = []
        self.player_turn = 1
        self.winner_found = False
        self.winner = 'a'
        self.width = 0
        self.row = 0
        self.column = 0
        for i in range(width):
            self.board.append([0]*width)
        for k in range(width):
            print(self.board[k])
    def turn(self, width):
        self.width = width
        print("It is Player "+ str(self.player_turn) +"'s turn.")
        while True:
            while True:
                try:
                    self.row = input("What row would you like to play in? ")
                    self.row = int(self.row)
                except Exception as e:
                    print("Please enter and integer 1 through " + str(width))
                else:
                    break
            while True:
                try:
                    self.column = input("What column would you like to play in? ")
                    self.column = int(self.column)
                except Exception as e:
                    print("Please enter and integer 1 through " + str(width))
                else:
                    break
            print("Player " + str(self.player_turn) + " is playing at row: " + str(self.row) + ", column: " + str(self.column))
            if self.board[self.row-1][self.column-1] != 0:
                print("This spot is already taken, please enter a valid unoccupied space.")
            else:
                break
        self.board[self.row-1][self.column-1] = self.player_turn


        run_again = True
        self.check_winner()
        if  self.winner_found:
            print("Player " + str(self.winner) + " wins!")
            exit()



        if self.player_turn == 1:
            self.player_turn = 2
        elif self.player_turn == 2:
            self.player_turn = 1
        if run_again:
            for k in range(self.width):
                print(self.board[k])
            self.turn(width)


    def check_winner(self):
        winner_found = False


b = Board(10)
for i in range(2):
    b.turn(10)


