def main():
    MAX_VALUE = 10000  # Constant value that sets the upper limit for Fibonacci numbers

    # Starting values of Fibonacci sequence
    a, b = 0, 1
    
    # Print Fibonacci numbers until we reach MAX_VALUE
    while a < MAX_VALUE:
        print(a, end=" ")  # Print the current Fibonacci number followed by a space
        a, b = b, a + b  # Update 'a' and 'b' to the next two Fibonacci numbers

# Ensure that the main function is called when the script runs
if __name__ == '__main__':
    main()
