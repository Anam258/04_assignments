def add_three_copies(my_list, data):
    """ Adds three copies of data to the given list (mutable behavior). """
    my_list.extend([data] * 3)  # Adds three copies of data to the list

def main():
    # User input
    message = input("Enter a message to copy: ")

    # Ensure that the input is not empty
    if not message:
        print("Please enter a valid message!")
        return

    # Empty list before modification
    my_list = []
    print("List before:", my_list)

    # Call the function (list changes without returning)
    add_three_copies(my_list, message)

    # List after modification
    print("List after:", my_list)

# Required line to run the program
if __name__ == '__main__':
    main()
