import random as rnd

class TicTacToe:
    def __init__(self, name): 
        self.name = name

    def welcome(self):
        """Welcome the player and show board."""
        print("Welcome ", self.name, ", to my tic-tac-toe.")     # Welcome
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        print("This is the game board.")
        for row in self.board:                       # Print board
            print(row)

    def sym(self): 
        """Choose a sym."""
        self.sym_1 = input("Choose your sym: X / O\n")
        while self.sym_1:
            if self.sym_1 == 'X':
                self.sym_2 = 'O'
                print("You are X.") 
                break               
            elif self.sym_1 == 'O':
                self.sym_2 == 'X'
                print("You are O.")
                break
            else:
                self.sym_1 = input("Please choose by typing 'X' or 'O'.\n")

    def start_game(self, count=1):
        """Start the game."""
        print("Let the game begin. :)")
        self.count = count
        while self.count:   
            if self.count == 1:
                if self.sym_1 == 'X':
                    print("X goes first. Choose the tile you wish to place your mark.")
                else:
                    print("X goes first. AI's turn.")
                    game.bot_player()
            elif self.count < 9:
                if self.count % 2 != 0:          # Odd num is player turn
                    print("Player ", self.sym, "'s turn.")
                else:
                    print("AI's turn.")     # Even num is AI turn
                    game.bot_player()
            elif self.count > 9:
                print("Draw. Game over.")
                break

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
            self.count +=1 
            game.update_board(self.sym_1)

    def bot_player(self):
        """Bot player."""
        self.row = rnd.randint(1,3)
        self.col = rnd.randint(1,3)
        game.update_board(self.sym_2)

    def update_board(self, sym):
        """Update board."""
        self.sym = sym
        self.board[self.row-1][self.col-1] = self.sym
        game.show_board()
        
    def show_board(self):
        """Show board."""
        print("Current board:")
        for row in self.board:
            print(row)

name = input("Your name: ")
game = TicTacToe(name)
game.welcome()
game.sym() 
game.start_game()