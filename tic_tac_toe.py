import random as rnd

class TicTacToe:
    def __init__(self, name): 
        self.name = name
        self.count = 0
        self.new_count = self.count

    def welcome(self):
        """Welcome the player and show board."""
        print("Welcome ", self.name.strip(), ", to my tic-tac-toe.")     # Welcome
        
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
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
                    self.play = False 
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
        row = input("Row: ")
        col = input("Col: ")
            
        self.take_input(row, col)

    def take_input(self, row, col):
        """Take input from human and AI."""                    
        while row:
            try:
                int(row)
            except ValueError:
                print("Please input an integer.")
                row = input("Row: ")
            else:
                row = int(row)   
                if (row>=1 and row<=3):
                    break
                else:
                    print("Please input an integer between 1 and 3.")
                    row = int(input("Row: "))

        while col:
            try:
                int(col)
            except ValueError:
                print("Please input an integer.")
                col = input("Col: ")
            else:
                col = int(col)
                if (col>=1 and col<=3):
                    break
                else:
                    print("Please input an integer from 1 to 3.")
                    col = int(input("Col: "))
        
        self.illegal(self.board, self.sym_bot, self.sym_player, row, col)
        game.update_board(self.sym_player, row, col)

    def bot_player(self):
        """Bot player."""
        row = rnd.randint(0,2)
        col = rnd.randint(0,2) 
        
        self.illegal(self.board, self.sym_bot, self.sym_player, row, col)
        game.update_board(self.sym_bot, row, col)

    def illegal(self, board, sym_bot, sym_player, row, col):
        """Check for occupied tiles."""
        while (self.board[row-1][col-1] == self.sym_bot) or (self.board[row-1][col-1] == self.sym_player):
            row = int(input("Pick another row: "))
            col = int(input("Pick another column: "))

    def win_game(self):
        """Check win condition."""
        winner = None
        # Check rows
        for row in range(0,3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == self.sym_player:
                print("Player (", self.sym_player, ") wins!")
                winner = True
            elif self.board[row][0] == self.board[row][1] == self.board[row][2] == self.sym_bot:
                print("AI (", self.sym_bot, ") wins!")
                winner = True
        
        # Check columns
        for column in range(0,3):
            if self.board[0][column] == self.board[1][column] == self.board[2][column] == self.sym_player:
                print("Player (", self.sym_player, ") wins!")
                winner = True
            elif self.board[0][column] == self.board[1][column] == self.board[2][column] == self.sym_bot:
                print("AI (", self.sym_bot, ") wins!")
                winner = True

        # Check diagonals 
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.sym_player:
            print("Player (", self.sym_player, ") wins!")
            winner = True
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == self.sym_bot:
            print("AI (", self.sym_bot, ") wins!")
            winner = True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == self.sym_player:
            print("Player (", self.sym_player, ") wins!")
            winner = True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == self.sym_bot:
            print("AI (", self.sym_bot, ") wins!")
            winner = True

        if winner == True:
            game.restart_game()

    def update_board(self, sym, row, col):
        """Update board."""
        self.symbol = sym
        self.board[row-1][col-1] = self.symbol
        game.show_board()
        game.win_game()
        
    def show_board(self):
        """Show board."""
        print("Current board:", self.new_count)
        for row in self.board:
            print(row)
        print("")
    
    def restart_game(self, ans='N'):
        """Ask user if they want to play again."""
        prompt = "Do you want to play again? Y / N\t"
        ans = input(prompt)
        if ans == 'Y':
            self.count == 0
            self.board = [[' ', ' ', ' '],
                          [' ', ' ', ' '],
                          [' ', ' ', ' ']]
            game.sym()
        elif ans == 'N':
            self.play = False

name = input("Your name: ")
game = TicTacToe(name)
game.welcome()
game.sym()
game.start_game()