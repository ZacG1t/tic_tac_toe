import numpy as np

# Welcome 
print("Welcome to my tic-tac-toe.")

# Game board
print("\nThis is the game board.")
board = [['1','2','3'],
         ['4','5','6'],
         ['7','8','9']]

for row in board: 
    print(row)

# Choosing side 
side = input("Choose your side: X / O\n")

#while side != ('X' or 'O'):
if side != ('X' or 'O'):
    side = input("Please choose by typing 'X' or 'O'.\n")
elif side == 'X':
    print("You are X.")
    #break
elif side == 'O':
    print("You are O.")
    #break

print("Let the game begin. :)")

