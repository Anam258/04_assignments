def main():
    count = 20  # Number of even numbers to print
    
    # Loop through numbers from 0 to 19 (20 iterations)
    for i in range(count):
        print(i * 2, end=" ")  # Multiply the index by 2 to get even numbers, print with space

# Ensures the main function is called when the script runs
if __name__ == '__main__':
    main()
