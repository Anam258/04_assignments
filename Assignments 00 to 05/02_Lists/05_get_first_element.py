def get_first_element(lst):
    """ Prints the first element of a given non-empty list. """
    if lst:  # Check if the list is not empty
        print("The first element in the list is:", lst[0])
    else:
        print("The list is empty, no first element!")

def main():

    n = int(input("Enter the number of elements in the list: "))
    
    if n <= 0:  # Basic check for non-positive input
        print("The list cannot be empty. Please enter a positive number.")
        return  # Exit the function if the list is empty
    
    lst = []
    
    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        lst.append(element)  # You can convert to int or float if needed
    
    get_first_element(lst)

# Required line to run the program
if __name__ == '__main__':
    main()
