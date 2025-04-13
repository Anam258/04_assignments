def sum_of_numbers(numbers):
    """
    This function takes a list of numbers and returns the sum of all the numbers in the list.
    """
    total = 0  # Initialize the total variable to 0
    
    # Iterate through each number in the list and add it to the total
    for num in numbers:
        total += num
    
    return total  # Return the sum of the numbers

def main():
    """
    Main function to demonstrate the sum_of_numbers function.
    It defines a list of numbers and prints the sum.
    """
    numbers_list = [10, 20, 30, 40, 50]  # List of numbers to sum
    result = sum_of_numbers(numbers_list)  # Calculate the sum using the sum_of_numbers function
    
    print("List:", numbers_list)  # Print the list of numbers
    print("Sum of numbers:", result)  # Print the sum of the numbers

# Run the main function if the script is executed directly
if __name__ == '__main__':
    main()
