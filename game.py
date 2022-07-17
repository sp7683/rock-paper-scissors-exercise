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

# DETERMINE THE WINNER AND DISPLAY RESULTS

if user_choice == computer_choice:
    print("You tied!")
elif user_choice == "Rock":
    if computer_choice == "Scissors":
        print("Rock crushes scissors. You win!")
    else:
        print("Paper covers rock. You lose.")
elif user_choice == "Paper":
    if computer_choice == "Rock":
        print("Paper covers rock. You win!")
    else:
        print("Scissors cuts paper. You lose.")
elif user_choice == "Scissors":
    if computer_choice == "Paper":
        print("Scissors cuts paper. You win!")
    else:
        print("Rock crushes scissors. You lose.")

# GOODBYE

print("Thanks 'Player One' for playing Rock, Paper, Scissors, Shoot! Please play again.")