import random  # Importing random module to generate random numbers

def main():
    # Generating a random number between 0 and 99
    secret_number = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99...")

    # Start a loop to let the user guess the number
    while True:
        try:
            # Asking the user to input a guess and converting it to an integer
            guess = int(input("Enter a guess: "))

            # Check if the guess is too high, too low, or correct
            if guess > secret_number:
                print("Your guess is too high.")
            elif guess < secret_number:
                print("Your guess is too low.")
            else:
                # If the guess is correct, print the success message and exit the loop
                print(f"Congrats! The number was: {secret_number}")
                break  # Exit the loop when the correct number is guessed
        except ValueError:
            # Handle the case where the user inputs a non-numeric value
            print("Please enter a valid number!")

# Calling the main function to start the game
if __name__ == '__main__':
    main()
