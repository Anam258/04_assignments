# Reverse Guess the Number Game - Python Project by Anam

import random

def computer_guess():
    print("Think of a number between 1 and 100, and I will try to guess it!")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0

    while True:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # or high, since both are same

        attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback == "c":
            print(f"Yay! I guessed your number in {attempts} attempts 🎉")
            break
        else:
            print("Please respond with 'H', 'L', or 'C'.")

# Call the function to run the game
computer_guess()

