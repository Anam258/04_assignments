def main():
    # Ask the user for a number and convert it to an integer
    curr_value = int(input("Enter a number: "))

    # Loop until curr_value is 100 or greater
    while curr_value < 100:
        curr_value *= 2  # Double the current value
        print(curr_value, end=" ")  # Print the updated value in the same line
    
# This line is required to call the main() function
if __name__ == '__main__':
    main()
