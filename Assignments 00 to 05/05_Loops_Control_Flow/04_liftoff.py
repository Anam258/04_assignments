import time  # Importing time module for delay

def main():
    # Countdown from 10 to 1
    for i in range(10, 0, -1):  # Starts from 10, goes to 1, decrementing by -1
        print(i, end=" ", flush=True)  # Print numbers in the same line with space
        time.sleep(1)  # Add a 1-second delay between each number
    print("Liftoff!")  # Print Liftoff! at the end

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
