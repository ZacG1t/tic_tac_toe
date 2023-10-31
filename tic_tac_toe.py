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
        self.sym_player = input("Choose your sym: X / O\n")
        if self.sym_player == 'X':
            self.sym_bot = 'O'
        else:
            self.sym_bot = 'X'
        while self.sym_player:
            if self.sym_player == 'X':
                print("You are X.") 
                break               
            elif self.sym_player == 'O':
                print("You are O.")
                break
            else:
                self.sym_player = input("Please choose by typing 'X' or 'O'.\n")

    def start_game(self):
        """Start the game."""
        count = 1
        self.count = count
        print("Let the game begin. :)")
        while self.count:   
            if self.count == 1:
                if self.sym_player == 'X':
                    print("X goes first. Player's turn.")
                elif self.sym_player == 'O':
                    print("X goes first. AI's turn.")
                    game.bot_player()
            elif (self.count > 1):                # Error block
                if self.sym_player == 'X':
                    if (self.count % 2 != 0):          # Odd num is player turn
                        print("Player ", self.sym_player.strip(), "'s turn.")
                    else:
                        print("AI's turn.")     # Even num is AI turn
                        game.bot_player()
                elif self.sym_player == 'O':
                    if (self.count % 2 != 0):
                        print("AI's turn")
                    else:
                        print("Player ", self.sym_player.strip(), "'s turn.") 
                
            if self.count > 9:
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
            self.count += 1 
            game.update_board(self.sym_player)

    def bot_player(self):
        """Bot player."""
        self.row = rnd.randint(1,3)
        self.col = rnd.randint(1,3)
        game.update_board(self.sym_bot)

    def update_board(self, sym):
        """Update board."""
        self.sym = sym
        self.board[self.row-1][self.col-1] = self.sym
        game.show_board()
        
    def show_board(self):
        """Show board."""
        print("Current board:", self.count)
        for row in self.board:
            print(row)

name = input("Your name: ")
game = TicTacToe(name)
game.welcome()
game.sym() 
game.start_game()