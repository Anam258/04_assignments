import random  # Import the random module to generate random numbers

def main():
    # Generate a list of 10 random integers between 1 and 100 (inclusive)
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    
    # Print the random numbers as space-separated values
    print(*random_numbers)

# Ensure that the main function is executed when the program is run directly
if __name__ == '__main__':
    main()
