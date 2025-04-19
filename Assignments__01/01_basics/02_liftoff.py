def main():
    # Starting countdown from 10 to 1 in reverse order
    for i in range(10, 0, -1):  # Countdown in reverse from 10 to 1
        print(i, end=" ")  # Print each number on the same line
    
    # Once the countdown is completed, print 'Liftoff!'
    print("Liftoff!")

# Ensuring the main function is called when the script is executed
if __name__ == '__main__':
    main()
