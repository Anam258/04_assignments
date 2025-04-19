# Rock, Paper, Scissors Game - Python Project by Anam

import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")

    options = ["rock", "paper", "scissors"]
    user = input("Choose rock, paper, or scissors: ").lower()
    
    if user not in options:
        print("Invalid choice. Please try again.")
        return

    computer = random.choice(options)
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win! 🎉")
    else:
        print("You lose. 😢")

# Run the game
play_game()
