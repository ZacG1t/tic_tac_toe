import random as rnd

class TicTacToe:
    def __init__(self, name): 
        self.name = name
        self.count = 0
        self.new_count = self.count

    def welcome(self):
        """Welcome the player and show board."""
        print("Welcome ", self.name, ", to my tic-tac-toe.")     # Welcome
        
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        
        self.data = {11:'', 12:'', 13:'',
                     21:'', 22:'', 23:'', 
                     31:'', 32:'', 33:'',}
        
        print("This is the game board.")
        game.show_board()

    def sym(self): 
        """Choose a sym."""
        self.sym_player = input("Choose your symbol: X / O\n")
        while self.sym_player == '':
            self.sym_player = input("Choose your symbol: X / O\n")
        while self.sym_player:
            if self.sym_player == 'X':
                self.sym_bot = 'O'
                print("You are X.") 
                break               
            elif self.sym_player == 'O':
                self.sym_bot = 'X'
                print("You are O.")
                break
            else:
                self.sym_player = input("Please choose by typing 'X' or 'O'.\n")
    
    def start_game(self):
        """Start the game."""
        print("Let the game begin. :)")
        # Game starts, check symbol
        self.new_count = 1
        self.play = True
        while self.play:
            if self.new_count == 1:
                if self.sym_player == 'X':
                    print("X goes first. Player's turn.")
                    game.human_player()
                else:
                    print("X goes first. AI's turn.")
                    game.bot_player()
            else:
                if self.new_count == 10:
                    print("Game over.")
                else:
                    if (self.new_count % 2 != 0):       # Odd number turn
                        if self.sym_player == 'X':
                            print("Player's turn.")
                            game.human_player()
                        else:
                            print("AI's turn.")
                            game.bot_player()
                    elif (self.new_count % 2 == 0):     # Even number turn
                        if self.sym_player == 'X':
                            print("AI's turn.")
                            game.bot_player()
                        else:
                            print("Player's turn.")
                            game.human_player()
            self.new_count += 1

    def human_player(self):
        """Take input from human player."""
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
                    print("Please input an integer from 1 to 3.")
                    self.col = input("Col: ")
                    self.col = int(self.col)
        game.update_board(self.sym_player)

    def bot_player(self):
        """Bot player."""
        self.row = rnd.randint(1,3)
        self.col = rnd.randint(1,3)
        game.update_board(self.sym_bot)

    def win_con(self):
        """Check win condition."""
        X = 0
        O = 0
        if self.count > 5:
            # Check horizontally 
            if self.data[11] == self.data[12] == self.data[13] == 'X':
                X = 1
            elif self.data[21] == self.data[22] == self.data[23] == 'X':
                X = 1
            elif self.data[31] == self.data[32] == self.data[33] == 'X':
                X = 1
            elif self.data[11] == self.data[12] == self.data[13] == 'O':
                O = 1
            elif self.data[21] == self.data[22] == self.data[23] == 'O':
                O = 1
            elif self.data[31] == self.data[32] == self.data[33] == 'O':
                O = 1
        # Show winner
        if X == 1:
            print("X wins!")
            #game.restart_game()
        elif O == 1:
            print("O wins!")
            #game.restart_game()

    def update_board(self, sym):
        """Update board."""
        self.symbol = sym
        self.board[self.row-1][self.col-1] = self.symbol
        coord =  int(self.row+self.col )
        self.data[coord] = self.symbol
        game.show_board()
        game.win_con()
        
    def show_board(self):
        """Show board."""
        print("Current board:", self.new_count)
        for row in self.board:
            print(row)
        print("")
    """
    def restart_game(self):
        Ask user if they want to play again.
        prompt = "Do you want to play again? Y / N\t"
        ans = input(prompt)
        if ans == 'Y':
            self.play = True
        elif ans == 'N':
            self.play = False
    """

name = input("Your name: ")
game = TicTacToe(name)
game.welcome()
game.sym()
game.start_game()