def main():
    # Initialize a dictionary to store the count of each number entered by the user
    num_counts = {}

    while True:
        # Prompt the user to enter a number. If the user presses Enter without entering a number, stop the loop.
        user_input = input("\033[94mEnter a number (or press Enter to stop): \033[0m")  # Blue text for input prompt
        
        # If user presses Enter without input, break the loop to stop the process
        if user_input == "":
            break
        
        # Convert the user input (string) to an integer
        try:
            number = int(user_input)
        except ValueError:
            # In case of non-numeric input, print a message and continue asking for input
            print("Please enter a valid number.")
            continue
        
        # Update the count of the number in the dictionary
        if number in num_counts:
            num_counts[number] += 1  # Increment the count if the number already exists
        else:
            num_counts[number] = 1  # Add the number to the dictionary with a count of 1

    # Print the count of each number entered
    print("\nNumber occurrences:")
    for num, count in num_counts.items():
        print(f"{num} appears {count} times.")

# Ensure the main function is executed when the program is run directly
if __name__ == '__main__':
    main()
