import random  # Importing the random module to generate random numbers

# Constants for the range and count of random numbers
N_NUMBERS: int = 10  # The number of random numbers to generate
MIN_VALUE: int = 1    # Minimum value for the random numbers
MAX_VALUE: int = 100  # Maximum value for the random numbers

def main():
    # Generate and print 10 random numbers in a single line
    for _ in range(N_NUMBERS):
        # Print each random number within the specified range
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")

    print()  # Printing a newline for better output formatting

# Ensuring the main function is called when the script is executed
if __name__ == '__main__':
    main()
