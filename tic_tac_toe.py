import numpy as np

# Welcome 
print("Welcome to my tic-tac-toe.")

# Game board
print("\nThis is the game board.")
board = [['-','-','-'],
         ['-','-','-'],
         ['-','-','-']]

for row in board: 
    print(row)

# Choosing side 
side = input("Choose your side: X / O\n")

while side != ('X' or 'O'):
    if side == 'X':
        print("You are X.")
        break
    elif side == 'O':
        print("You are O.")
        break
    else:
        side = input("Please choose by typing 'X' or 'O'.\n")

print("Let the game begin. :)")