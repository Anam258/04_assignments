# Guess the Number Game - Python Project by Anam

import random

# Step 1: Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Step 2: Set initial guess count
attempts = 0

print("Welcome to the Guess the Number Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

# Step 3: Start the guessing loop
while True:
    guess = input("Enter your guess: ")

    # Check if input is a valid number
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} tries 🎉")
        break
