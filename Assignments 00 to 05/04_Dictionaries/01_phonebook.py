def read_phone_numbers():
    """
    Function to read phone numbers and store them in a dictionary.
    User can input names and corresponding phone numbers until an empty name is entered.
    Returns the phonebook dictionary.
    """
    phonebook = {}

    while True:
        # Prompt user to enter a name (empty name will stop input)
        name = input("Name: ")
        if name == "":
            break  # Exit the loop if the name is empty
        # Prompt user to enter the corresponding phone number
        number = input("Number: ")
        # Store name and number in the phonebook dictionary
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    """
    Function to print the phonebook. Each entry is printed as "Name -> Phone Number".
    """
    print("\nPhonebook Entries:")
    for name, number in phonebook.items():
        print(f"{name} -> {number}")


def lookup_number(phonebook):
    """
    Function to look up a phone number by name.
    Continues prompting for names until an empty name is entered.
    If the name is not in the phonebook, informs the user.
    """
    while True:
        # Prompt the user to enter a name to look up
        name = input("Enter name to lookup: ")
        if name == "":
            break  # Exit the loop if the input is empty
        
        # Check if the name exists in the phonebook and print the number
        if name not in phonebook:
            print(f"{name} is not in the phonebook.")
        else:
            print(f"{name}'s phone number: {phonebook[name]}")


def main():
    """
    Main function to run the phonebook program.
    It reads phone numbers, prints the phonebook, and performs lookups.
    """
    phonebook = read_phone_numbers()  # Read phone numbers into a dictionary
    print_phonebook(phonebook)  # Print the entire phonebook
    lookup_number(phonebook)  # Perform number lookups based on user input


# This line ensures the main function runs when the script is executed directly
if __name__ == '__main__':
    main()
