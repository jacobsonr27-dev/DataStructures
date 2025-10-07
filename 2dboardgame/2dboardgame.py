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
            printable = ''
            for y in self.board[k]:
                printable = printable + str(y) + '  '
            print(printable)
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
            if self.board[self.row][self.column] != 0:
                print("This spot is already taken, please enter a valid unoccupied space.")
            else:
                break
        self.board[self.row][self.column] = self.player_turn


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
                printable = ''
                for y in self.board[k]:
                    printable = printable + str(y) + '  '
                print(printable)

            self.turn(width)


    def check_winner(self):
        try:
            if self.board[self.row][self.column] == self.board[self.row][self.column-1] and self.board[self.row][self.column] == self.board[self.row][self.column-2] and self.board[self.row][self.column] == self.board[self.row][self.column-3] and self.board[self.row][self.column] == self.board[self.row][self.column-4] and self.board[self.row][self.column] == self.board[self.row][self.column-5]:
                self.winner_found = True
        except IndexError or self.winner_found == False:
            try:
                if self.board[self.row][self.column] == self.board[self.row][self.column+1] and self.board[self.row][self.column] == self.board[self.row][self.column-1] and self.board[self.row][self.column] == self.board[self.row][self.column-2] and self.board[self.row][self.column] == self.board[self.row][self.column-3] and self.board[self.row][self.column] == self.board[self.row][self.column-4]:
                    self.winner_found = True
            except IndexError or self.winner_found == False:
                try:
                    if self.board[self.row][self.column] == self.board[self.row][self.column+2] and self.board[self.row][self.column] == self.board[self.row][self.column+1] and self.board[self.row][self.column] == self.board[self.row][self.column-1] and self.board[self.row][self.column] == self.board[self.row][self.column-2] and self.board[self.row][self.column] == self.board[self.row][self.column-3]:
                        self.winner_found = True
                except IndexError or self.winner_found == False:
                    try:
                        if self.board[self.row][self.column] == self.board[self.row][self.column+3] and self.board[self.row][self.column] == self.board[self.row][self.column+2] and self.board[self.row][self.column] == self.board[self.row][self.column+1] and self.board[self.row][self.column] == self.board[self.row][self.column-1] and self.board[self.row][self.column] == self.board[self.row][self.column-2]:
                            self.winner_found = True
                    except IndexError or self.winner_found == False:
                        try:
                            if self.board[self.row][self.column] == self.board[self.row][self.column+4] and self.board[self.row][self.column] == self.board[self.row][self.column+3] and self.board[self.row][self.column] == self.board[self.row][self.column+2] and self.board[self.row][self.column] == self.board[self.row][self.column+1] and self.board[self.row][self.column] == self.board[self.row][self.column-1]:
                                self.winner_found = True
                        except IndexError or self.winner_found == False:
                            try:
                                if self.board[self.row][self.column] == self.board[self.row][self.column+5] and self.board[self.row][self.column] == self.board[self.row][self.column+4] and self.board[self.row][self.column] == self.board[self.row][self.column+3] and self.board[self.row][self.column] == self.board[self.row][self.column+2] and self.board[self.row][self.column] == self.board[self.row][self.column+1]:
                                    self.winner_found = True
                            except IndexError or self.winner_found == False:
                                pass
        try:
            if self.board[self.row][self.column] == self.board[self.row-1][self.column] and self.board[self.row][self.column] == self.board[self.row-2][self.column] and self.board[self.row][self.column] == self.board[self.row-3][self.column] and self.board[self.row-4][self.column] == self.board[self.row][self.column] and self.board[self.row][self.column] == self.board[self.row-5][self.column]:
                self.winner_found = True
        except IndexError:
            pass
        try:
            if self.board[self.row][self.column] == self.board[self.row+1][self.column] and self.board[self.row][self.column] == self.board[self.row-1][self.column] and self.board[self.row][self.column] == self.board[self.row-2][self.column] and self.board[self.row-3][self.column] == self.board[self.row][self.column] and self.board[self.row][self.column] == self.board[self.row-4][self.column]:
                self.winner_found = True
        except IndexError:
            pass
        try:
            if self.board[self.row][self.column] == self.board[self.row+2][self.column] and self.board[self.row][self.column] == self.board[self.row+1][self.column] and self.board[self.row][self.column] == self.board[self.row-1][self.column] and self.board[self.row-2][self.column] == self.board[self.row][self.column] and self.board[self.row][self.column] == self.board[self.row-3][self.column]:
                self.winner_found = True
        except IndexError:
            pass
        try:
            if self.board[self.row][self.column] == self.board[self.row+3][self.column] and self.board[self.row][self.column] == self.board[self.row+2][self.column] and self.board[self.row][self.column] == self.board[self.row+1][self.column] and self.board[self.row-1][self.column] == self.board[self.row][self.column] and self.board[self.row][self.column] == self.board[self.row-2][self.column]:
                self.winner_found = True
        except IndexError:
            pass
        try:
            if self.board[self.row][self.column] == self.board[self.row+4][self.column] and self.board[self.row][self.column] == self.board[self.row+3][self.column] and self.board[self.row][self.column] == self.board[self.row+2][self.column] and self.board[self.row+1][self.column] == self.board[self.row][self.column] and self.board[self.row][self.column] == self.board[self.row-1][self.column]:
                self.winner_found = True
        except IndexError:
            pass
        try:
            if self.board[self.row][self.column] == self.board[self.row+5][self.column] and self.board[self.row][self.column] == self.board[self.row+4][self.column] and self.board[self.row][self.column] == self.board[self.row+3][self.column] and self.board[self.row+2][self.column] == self.board[self.row][self.column] and self.board[self.row][self.column] == self.board[self.row+1][self.column]:
                self.winner_found = True
        except IndexError:
            pass

        try:
            if self.board[self.row][self.column] == self.board[self.row-1][self.column+1] and self.board[self.row][self.column] == self.board[self.row-2][self.column+2] and self.board[self.row][self.column] == self.board[self.row-3][self.column+3] and self.board[self.row-4][self.column+4] == self.board[self.row][self.column] and self.board[self.row][self.column] == self.board[self.row-5][self.column+5]:
                self.winner_found = True
        except IndexError:
            pass
        try:
            if self.board[self.row][self.column] == self.board[self.row+1][self.column-1] and self.board[self.row][self.column] == self.board[self.row-1][self.column+1] and self.board[self.row][self.column] == self.board[self.row-2][self.column+2] and self.board[self.row-3][self.column+3] == self.board[self.row][self.column] and self.board[self.row][self.column] == self.board[self.row-4][self.column+4]:
                self.winner_found = True
        except IndexError:
            pass
        try:
            if self.board[self.row][self.column] == self.board[self.row+2][self.column-2] and self.board[self.row][self.column] == self.board[self.row+1][self.column-1] and self.board[self.row][self.column] == self.board[self.row-1][self.column+1] and self.board[self.row-2][self.column+2] == self.board[self.row][self.column] and self.board[self.row][self.column] == self.board[self.row-3][self.column+3]:
                self.winner_found = True
        except IndexError:
            pass
        try:
            if self.board[self.row][self.column] == self.board[self.row+3][self.column-3] and self.board[self.row][self.column] == self.board[self.row+2][self.column-2] and self.board[self.row][self.column] == self.board[self.row+1][self.column-1] and self.board[self.row-1][self.column+1] == self.board[self.row][self.column] and self.board[self.row][self.column] == self.board[self.row-2][self.column+2]:
                self.winner_found = True
        except IndexError:
            pass
        try:
            if self.board[self.row][self.column] == self.board[self.row+4][self.column-4] and self.board[self.row][self.column] == self.board[self.row+3][self.column-3] and self.board[self.row][self.column] == self.board[self.row+2][self.column-2] and self.board[self.row+1][self.column-1] == self.board[self.row][self.column] and self.board[self.row][self.column] == self.board[self.row-1][self.column+1]:
                self.winner_found = True
        except IndexError:
            pass
        try:
            if self.board[self.row][self.column] == self.board[self.row+5][self.column-5] and self.board[self.row][self.column] == self.board[self.row+4][self.column-4] and self.board[self.row][self.column] == self.board[self.row+3][self.column-3] and self.board[self.row+2][self.column-2] == self.board[self.row][self.column] and self.board[self.row][self.column] == self.board[self.row+1][self.column-1]:
                self.winner_found = True
        except IndexError:
            pass

        try:
            if self.board[self.row][self.column] == self.board[self.row-1][self.column-1] and self.board[self.row][self.column] == self.board[self.row-2][self.column-2] and self.board[self.row][self.column] == self.board[self.row-3][self.column-3] and self.board[self.row-4][self.column-4] == self.board[self.row][self.column] and self.board[self.row][self.column] == self.board[self.row-5][self.column-5]:
                self.winner_found = True
        except IndexError:
            pass
        try:
            if self.board[self.row][self.column] == self.board[self.row+1][self.column+1] and self.board[self.row][self.column] == self.board[self.row-1][self.column-1] and self.board[self.row][self.column] == self.board[self.row-2][self.column-2] and self.board[self.row-3][self.column-3] == self.board[self.row][self.column] and self.board[self.row][self.column] == self.board[self.row-4][self.column-4]:
                self.winner_found = True
        except IndexError:
            pass
        try:
            if self.board[self.row][self.column] == self.board[self.row+2][self.column+2] and self.board[self.row][self.column] == self.board[self.row+1][self.column+1] and self.board[self.row][self.column] == self.board[self.row-1][self.column-1] and self.board[self.row-2][self.column-2] == self.board[self.row][self.column] and self.board[self.row][self.column] == self.board[self.row-3][self.column-3]:
                self.winner_found = True
        except IndexError:
            pass
        try:
            if self.board[self.row][self.column] == self.board[self.row+3][self.column+3] and self.board[self.row][self.column] == self.board[self.row+2][self.column+2] and self.board[self.row][self.column] == self.board[self.row+1][self.column+1] and self.board[self.row-1][self.column-1] == self.board[self.row][self.column] and self.board[self.row][self.column] == self.board[self.row-2][self.column-2]:
                self.winner_found = True
        except IndexError:
            pass
        try:
            if self.board[self.row][self.column] == self.board[self.row+4][self.column+4] and self.board[self.row][self.column] == self.board[self.row+3][self.column+3] and self.board[self.row][self.column] == self.board[self.row+2][self.column+2] and self.board[self.row+1][self.column+1] == self.board[self.row][self.column] and self.board[self.row][self.column] == self.board[self.row-1][self.column-1]:
                self.winner_found = True
        except IndexError:
            pass
        try:
            if self.board[self.row][self.column] == self.board[self.row+5][self.column+5] and self.board[self.row][self.column] == self.board[self.row+4][self.column+4] and self.board[self.row][self.column] == self.board[self.row+3][self.column+3] and self.board[self.row+2][self.column+2] == self.board[self.row][self.column] and self.board[self.row][self.column] == self.board[self.row+1][self.column+1]:
                self.winner_found = True
        except IndexError:
            pass







b = Board(10)
for i in range(2):
    b.turn(10)


