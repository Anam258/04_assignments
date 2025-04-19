def main():
    # Prompting user to input a number and convert it to an integer
    user_value = int(input("Please enter a number: "))
    
    # Loop will continue until the value reaches or exceeds 100
    while user_value < 100:
        user_value *= 2  # Doubling the current value
        print(user_value, end=" ")  # Display the updated value on the same line

# Ensuring that the main function runs when the script is executed
if __name__ == '__main__':
    main()
