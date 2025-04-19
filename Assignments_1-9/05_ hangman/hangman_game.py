# Hangman Game - Python Project by Anam

import random
import string

def hangman():
    # List of words for the game
    words = ["python", "hangman", "code", "keyboard", "program", "developer"]
    word = random.choice(words).lower()  # Randomly pick a word
    word_letters = set(word)  # Unique letters in the word
    alphabet = set(string.ascii_lowercase)  # Valid letters
    used_letters = set()  # Letters guessed by the user

    lives = 6  # Number of allowed wrong guesses

    print("Welcome to Hangman!")
    
    # Game loop
    while len(word_letters) > 0 and lives > 0:
        # Show the current progress
        print("\nYou have", lives, "lives left. Used letters:", " ".join(used_letters))

        # Display the word with guessed letters
        word_display = [letter if letter in used_letters else "_" for letter in word]
        print("Current word: ", " ".join(word_display))

        # Get user input
        user_letter = input("Guess a letter: ").lower()

        # Check valid input
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Correct!")
            else:
                lives -= 1
                print("Wrong! That letter is not in the word.")
        elif user_letter in used_letters:
            print("You already guessed that letter.")
        else:
            print("Invalid character. Please guess a letter.")

    # End of game
    if lives == 0:
        print("\nYou died. The word was:", word)
    else:
        print("\nCongratulations! You guessed the word:", word)

# Run the game
hangman()
