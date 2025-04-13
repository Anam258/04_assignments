import random  # Import the random module to generate random numbers

NUM_SIDES: int = 6  # Define the number of sides on each die

def main():
    """
    This function simulates rolling two dice, calculates the total of both dice,
    and prints the individual results and the total sum.
    """
    
    # Roll the first die and get a random number between 1 and NUM_SIDES (inclusive)
    die1: int = random.randint(1, NUM_SIDES)
    
    # Roll the second die and get a random number between 1 and NUM_SIDES (inclusive)
    die2: int = random.randint(1, NUM_SIDES)
    
    # Calculate the total of both dice
    total: int = die1 + die2

    # Print the results
    print("Dice have", NUM_SIDES, "sides each.")  # Display the number of sides on the dice
    print("First die:", die1)  # Show the result of the first die
    print("Second die:", die2)  # Show the result of the second die
    print("Total of two dice:", total)  # Show the total sum of both dice

# Ensure that the main function runs when the script is executed
if __name__ == '__main__':
    main()
