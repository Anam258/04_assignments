import random

def main():
    # Generate a secret number between 0 and 99
    secret_number = random.randint(0, 99)  
    print("I am thinking of a number between 0 and 99...")

    while True:
        try:
            # Prompt user to enter a guess
            guess = int(input("Enter a guess: "))  

            # Check if the guess is too low, too high, or correct
            if guess < secret_number:
                print("Your guess is too low")
            elif guess > secret_number:
                print("Your guess is too high")
            else:
                print(f"Congrats! The number was: {secret_number}")
                break  # Exit the loop when the guess is correct
        except ValueError:
            # Handle non-integer input gracefully
            print("Please enter a valid number!")  

# Ensure the main function is called when the script runs
if __name__ == '__main__':
    main()
