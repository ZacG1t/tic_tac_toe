class TicTacToe:
    def __init__(self, name): 
        self.name = name        # Useful for future leaderboard function

    def welcome(self):
        """Welcome the player and show empty board."""
        print("Welcome ", self.name, ", to my tic-tac-toe.")     # Welcome

        print("\nThis is the game board.")      # Empty board
        self.board = [['-', '-', '-'],
                ['-', '-', '-'],
                ['-', '-', '-']]

        for row in self.board:                       # Print board
            print(row)

    def side(self): 
        """Choose a side."""
        side = input("Choose your side: X / O\n")

        if side != ('X' or 'O'):
            side = input("Please choose by typing 'X' or 'O'.\n")
        elif side == 'X':
            print("You are X.")
        elif side == 'O':
            print("You are O.")

    def start_game(self):
        print("Let the game begin. :)")
        print("X goes first. Choose the tile you wish to place your mark.")
        self.row = int(input("Row: "))
        if type(self.row) != int: 
            self.row = input("Please input an integer.\n")
        
        self.col = int(input("Column: "))
        if type(self.col) != int:
            self.col = input("Please input an integer.\n")

    def update_board(self):
        self.board[self.row-1][self.col-1] = 'X'
        for row in self.board:
            print(row)

game = TicTacToe("TEO")
game.welcome()
game.side() 
game.start_game()
game. update_board()