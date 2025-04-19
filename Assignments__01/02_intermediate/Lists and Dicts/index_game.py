# A program to perform list operations like access, modify, and slice

def access_element(my_list, index):
    """Return the element at the specified index, or an error if out of range."""
    if 0 <= index < len(my_list):
        return f"Element at index {index}: {my_list[index]}"
    return "Error: Index is out of range!"

def modify_element(my_list, index, new_value):
    """Update the element at the given index with a new value, or return an error."""
    if 0 <= index < len(my_list):
        my_list[index] = new_value
        return f"List after modification: {my_list}"
    return "Error: Index is out of range!"

def slice_list(my_list, start, end):
    """Return a portion of the list based on start and end indices, with validation."""
    if 0 <= start < len(my_list) and 0 < end <= len(my_list) and start < end:
        return f"Sliced list from index {start} to {end - 1}: {my_list[start:end]}"
    return "Error: Invalid slicing indices!"

def main():
    # Sample list to perform operations on
    my_list = ["apple", "banana", "cherry", "date", "elderberry"]

    print("Welcome to the List Operations Program!")
    
    while True:
        # Displaying operation menu
        print("\nSelect an operation to perform:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            index = int(input("Enter the index you want to access: "))
            print(access_element(my_list, index))

        elif choice == "2":
            index = int(input("Enter the index you want to modify: "))
            new_value = input("Enter the new value: ")
            print(modify_element(my_list, index, new_value))

        elif choice == "3":
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            print(slice_list(my_list, start, end))

        elif choice == "4":
            print("Thank you for using the List Operations Program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 4.")

# Entry point of the program
if __name__ == "__main__":
    main()
