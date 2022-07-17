# this is the "game.py" file...

# dependencies

import random

print("Welcome 'Player One' to Rock, Paper, Scissors, Shoot!")

# USER INPUTS

user_choice = input("Please select 'Rock', 'Paper', 'Scissors':") 
print(f"You chose: '{user_choice}'")


# VALIDATE USER INPUTS




# COMPUTER CHOICE

options = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(options)

print(f"The computer chose: '{computer_choice}'")

# DETERMINE THE WINNER




# DISPLAY RESULTS

#
#-------------------
#Welcome 'Player One' to my Rock-Paper-Scissors game...
#-------------------
#Please choose either 'rock', 'paper', or 'scissors': rock
#You chose: 'rock'
#The computer chose: 'paper'
#-------------------
#Oh, the computer won. It's ok.
#-------------------
#Thanks for playing. Please play again!
#
