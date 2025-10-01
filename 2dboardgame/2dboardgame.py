class Board:
    def __init__(self, width):
        self.board = []
        for i in range(width):
            self.board.append([0]*width)
        for k in range(width):
            print(self.board[k])
    def turn(self, width):
        player_turn = 1
        print("It is Player "+ str(player_turn) +"'s turn.")
        while True:
            while True:
                try:
                    row = input("What row would you like to play in? ")
                    row = int(row)
                except Exception as e:
                    print("Please enter and integer 1 through " + str(width))
                else:
                    break
            while True:
                try:
                    column = input("What column would you like to play in? ")
                    column = int(column)
                except Exception as e:
                    print("Please enter and integer 1 through " + str(width))
                else:
                    break
            print("Player " + str(player_turn) + " is playing at row: " + str(row) + ", column: " + str(column))
            if self.board[row-1][column-1] != 0:
                print("This spot is already taken, please enter a valid unoccupied space.")
            else:
                break
        self.board[row-1][column-1] = player_turn
        if player_turn == 1:
            player_turn = 2
        else:
            player_turn = 1
        for k in range(width):
            print(self.board[k])




b = Board(10)

b.turn(10)

