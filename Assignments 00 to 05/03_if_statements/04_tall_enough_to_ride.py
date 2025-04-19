def main():
    # Start an infinite loop to repeatedly ask for the user's height
    while True:
        # Prompt the user to enter their height
        height = (input("How tall are you? "))

        # If the user presses Enter without typing anything, exit the program
        if height == "":
            print("Exiting the program. Have a great day!")
            break

        # Convert the input from a string to an integer for comparison
        height = float(height)

        # Check if the user's height meets or exceeds the minimum height requirement
        if height >= 50:
            print("You're tall enough to ride!\n")
        else:
            print("You're not tall enough to ride, but maybe next year!\n")

# Ensure that the main function is called when the program is executed directly
if __name__ == '__main__':
    main()
