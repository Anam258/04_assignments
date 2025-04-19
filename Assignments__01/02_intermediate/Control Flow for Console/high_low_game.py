import random  # Importing the random module to generate random numbers

# Constants
NUM_ROUNDS = 5  # Total number of rounds in the game

def main():
    # Welcome message
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    score = 0  # Initialize score to 0
    
    # Loop to play multiple rounds
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        # Generate random numbers for the user and the computer
        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        # Display user's number
        print(f"Your number is {user_number}")

        # Loop for valid input on guessing 'higher' or 'lower'
        while True:
            guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
            if guess in ["higher", "lower"]:
                break  # Break the loop if valid input
            print("Invalid input! Please enter either 'higher' or 'lower'.")  # Prompt if invalid input
        
        # Determine if the user's guess was correct
        if (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
            print("You were right!", end=" ")  # If guess is correct, increase score
            score += 1
        else:
            print("Aww, that's incorrect.", end=" ")  # If guess is incorrect, no score change

        # Reveal the computer's number and current score
        print(f"The computer's number was {computer_number}")
        print(f"Your score is now {score}\n")

    # Display the final message based on score
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")  # Perfect score message
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")  # Half or more correct answers
    else:
        print("Better luck next time!")  # Less than half correct answers

# Ensure the main function is executed when running the script
if __name__ == '__main__':
    main()
