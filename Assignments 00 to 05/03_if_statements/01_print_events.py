# Program to print the first 20 even numbers using a loop

def print_even_numbers():
    # Loop to iterate 20 times (from 0 to 19)
    for counter in range(20):
        even_number = counter * 2  # Calculate even number by multiplying with 2
        print(even_number, end=" ")  # Print the even number with space instead of newline

# Entry point of the program
if __name__ == '__main__':
    print_even_numbers()
