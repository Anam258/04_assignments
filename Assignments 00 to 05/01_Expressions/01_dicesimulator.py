"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times. Prints
the results of each die roll. This program is used
to show how variable scope works.
"""

import random  # Importing the random module to generate random numbers

NUM_SIDES = 6  # Constant representing the number of sides on each die

def roll_dice():
    """
    Simulate rolling two dice and print their results.
    Each die generates a random integer between 1 and NUM_SIDES (inclusive).
    The total sum of both dice is calculated and printed.
    """
    die1 = random.randint(1, NUM_SIDES)  # Generate a random number for die 1
    die2 = random.randint(1, NUM_SIDES)  # Generate a random number for die 2
    total = die1 + die2  # Calculate the total of both dice
    # Print the result of the dice roll with the individual dice and their sum
    print(f"Die 1: {die1}, Die 2: {die2} → Total: {total}")

def main():
    """
    The main function of the program where the dice rolls are simulated.
    It demonstrates how variable scope works by showing the value of die1
    before and after calling the roll_dice() function.
    """
    die1 = 10  # Local variable die1 is assigned a value of 10 in main()
    print(f"die1 in main() starts as: {die1}")  # Print the initial value of die1

    # Loop to simulate rolling the dice three times
    for _ in range(3):
        roll_dice()  # Call the roll_dice function

    # The local variable die1 in main() is unaffected by the roll_dice() function
    print(f"die1 in main() is still: {die1}")  # Print the final value of die1, showing no change

# Ensure the main function is called when the script is executed
if __name__ == '__main__':
    main()
