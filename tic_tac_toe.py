class TicTacToe:
    def __init__(self, name): 
        self.name = name        # Useful for future leaderboard function

    def welcome(self):
        """Welcome the player and show board."""
        print("Welcome ", self.name, ", to my tic-tac-toe.")     # Welcome
        self.board = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]
        print("This is the game board.")
        for row in self.board:                       # Print board
            print(row)

    def side(self): 
        """Choose a side."""
        self.side = input("Choose your side: X / O\n")

        if self.side != ('X' or 'O'):
            side = input("Please choose by typing 'X' or 'O'.\n")
        elif self.side == 'X':
            print("You are X.")
        elif self.side == 'O':
            print("You are O.")

    def start_game(self):

        print("Let the game begin. :)")
        if self.side == 'X':
            print("X goes first. Choose the tile you wish to place your mark.")
        elif self.side == 'O':
            print("X goes first.")

        self.row = input("Row: ")
        while self.row:
            try:
                int(self.row)
            except ValueError:
                print("Please input an integer.")
                self.row = input("Row: ")
            else:
                self.row = int(self.row)   
                if (self.row>=1 and self.row<=3):
                    break
                else:
                    print("Please input an integer between 1 and 3.")
                    self.row = input("Row: ")
                    self.row = int(self.row)
                

        self.col = input("Col: ")
        while self.col:
            try:
                int(self.col)
            except ValueError:
                print("Please input an integer.")
                self.col = input("Col: ")
            else:
                self.col = int(self.col)
                if (self.col>=1 and self.col<=3):
                    break
                else:
                    print("Please input an integer fro 1 to 3.")
                    self.col = input("Col: ")
                    self.col = int(self.col)
        game.update_board()

    def update_board(self):
        self.board[self.row-1][self.col-1] = 'X'
        print("Current board:")
        for row in self.board:
            print(row)

name = input("Your name: ")
game = TicTacToe(name)
game.welcome()
game.side() 
game.start_game()