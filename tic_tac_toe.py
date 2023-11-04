import random as rnd

class TicTacToe:
    def __init__(self, name): 
        self.name = name

    def welcome(self):
        """Welcome the player and show board."""
        print("Welcome ", self.name.strip(), ", to my tic-tac-toe.")     # Welcome
        turn = 0
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        print("This is the game board.")
        game.show_board(turn)
        game.sym(turn)

    def sym(self, count=0): 
        """Choose a sym."""
        turn = count
        self.sym_player = input("Choose your symbol: X / O\n")
        while self.sym_player == '':
            self.sym_player = input("Choose your symbol: X / O\n")
        while self.sym_player:
            if self.sym_player == 'X':
                self.sym_bot = 'O'
                print("You are X.") 
                turn = 1
                game.start_game(count=turn, start=True)
                break               
            elif self.sym_player == 'O':
                self.sym_bot = 'X'
                print("You are O.")
                turn = 1
                game.start_game(count=turn, start=True)
                break
            else:
                self.sym_player = input("Please choose by typing 'X' or 'O'.\n")

    def start_game(self, count, start=False):
        """Start the game."""
        # Game starts, check symbol
        turn = count
        play = start
        if play == 1:
            while play ==  1:
                if turn == 1:
                    print("Let the game begin. :)")
                    if self.sym_player == 'X':
                        print("X goes first. Player's turn.")
                        game.human_player(count=turn)
                    else:
                        print("X goes first. AI's turn.")
                        game.bot_player(turn)
                else:
                    if turn == 10:
                        play = 0 
                        print("Draw. Game over.")
                    else:
                        if (turn % 2 != 0):       # Odd number turn
                            if self.sym_player == 'X':
                                print("Player's turn.")
                                game.human_player(turn)
                            else:
                                print("AI's turn.")
                                game.bot_player(turn)
                        elif (turn % 2 == 0):     # Even number turn
                            if self.sym_player == 'X':
                                print("AI's turn.")
                                game.bot_player(count=turn)
                            else:
                                print("Player's turn.")
                                game.human_player(turn)
        elif play == 0:
            None


    def human_player(self, count):
        """Take input from human player."""
        turn = count
        row = input("Row: ")
        col = input("Col: ")
            
        self.take_input(row, col, turn)

    def take_input(self, row, col, count):
        """Take input from human and AI."""                    
        turn = count
        while (turn > 0):
            try:
                int(row)
            except ValueError:
                print("Please input an integer.")
                row = input("Row: ")
            except:
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
            except:
                print("Please input an integer.")
                col = input("Col: ")
            else:
                col = int(col)
                if (col>=1 and col<=3):
                    break
                else:
                    print("Please input an integer from 1 to 3.")
                    col = int(input("Col: "))
        
        self.illegal(self.board, self.sym_bot, self.sym_player, row, col, turn)
        game.update_board(self.sym_player, row, col, turn)

    def bot_player(self, count):
        """Bot player."""
        turn = count
        if turn > 0:
            row = rnd.randint(0,2)
            col = rnd.randint(0,2) 
            
            self.illegal(self.board, self.sym_bot, self.sym_player, row, col, turn)
            game.update_board(self.sym_bot, row, col, turn)
        else:
            None

    def illegal(self, board, sym_bot, sym_player, row, col, count):
        """Check for occupied tiles."""
        turn = count
        while (self.board[row-1][col-1] == self.sym_bot) or (self.board[row-1][col-1] == self.sym_player):
            if (turn % 2 != 0):
                if (self.sym_player == 'X'):
                    row = int(input("Pick another row: "))
                    col = int(input("Pick another column: "))
                else:
                    game.bot_player(count=turn)
            elif (turn % 2 == 0):
                if (self.sym_player == 'X'):
                    game.bot_player(turn)
                else:
                    row = int(input("Pick another row: "))
                    col = int(input("Pick another column: "))

    def win_game(self, count):
        """Check win condition."""
        winner = None
        turn = count
        # Check rows
        for row in range(0,3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == self.sym_player:
                print("Player (", self.sym_player, ") wins!")
                winner = True
                play = 0
            elif self.board[row][0] == self.board[row][1] == self.board[row][2] == self.sym_bot:
                print("AI (", self.sym_bot, ") wins!")
                winner = True
                play = 0

        # Check columns
        for column in range(0,3):
            if self.board[0][column] == self.board[1][column] == self.board[2][column] == self.sym_player:
                print("Player (", self.sym_player, ") wins!")
                winner = True
                play = 0
            elif self.board[0][column] == self.board[1][column] == self.board[2][column] == self.sym_bot:
                print("AI (", self.sym_bot, ") wins!")
                winner = True
                play = 0

        # Check diagonals 
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.sym_player:
            print("Player (", self.sym_player, ") wins!")
            winner = True
            play = 0
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == self.sym_bot:
            print("AI (", self.sym_bot, ") wins!")
            winner = True
            play = 0
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == self.sym_player:
            print("Player (", self.sym_player, ") wins!")
            winner = True
            play = 0
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == self.sym_bot:
            print("AI (", self.sym_bot, ") wins!")
            winner = True
            play = 0

        if winner == True:
            game.restart_game()
            return play
            
    def update_board(self, sym, row, col, count):
        """Update board."""
        symbol = sym
        turn = count
        self.board[row-1][col-1] = symbol
        game.show_board(turn)
        game.win_game(turn)
        turn = turn + 1
        game.start_game(count=turn, start=True)
        
    def show_board(self, count):
        """Show board."""
        turn = count
        print("Current board:", turn)
        for row in self.board:
            print(row)
        print("")
        return turn
    
    def restart_game(self, ans='N'):
        """Ask user if they want to play again."""
        prompt = "\nDo you want to play again? Y / N\t"
        ans = input(prompt)
        if ans == 'N':
            play = 0
            self.board = [[' ', ' ', ' '],
                          [' ', ' ', ' '],
                          [' ', ' ', ' ']]
            self.end_game()
        else:
            turn = 0
            self.board = [[' ', ' ', ' '],
                          [' ', ' ', ' '],
                          [' ', ' ', ' ']]
            game.sym(turn)
            
    def end_game(self, count=0):
        """End and bye."""
        play = 0 
        turn = count
        game.start_game(count=turn, start=play)
        print("Goodbye.")

name = input("Your name: ")
game = TicTacToe(name)
game.welcome()