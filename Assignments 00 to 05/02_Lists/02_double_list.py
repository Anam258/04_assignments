def main():
    # Define a list of numbers
    numbers = [1, 2, 3, 4]

    # Loop through each element in the list and multiply it by 2
    for i in range(len(numbers)):
        numbers[i] *= 2  # Double the value at the current index

    # Print the modified list after doubling the values
    print("Doubled List:", numbers)

# Ensure the main function is called when the script is run directly
if __name__ == '__main__':
    main()
