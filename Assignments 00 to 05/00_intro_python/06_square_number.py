def main():
    try:
        # Prompt the user to enter a number
        number = float(input("Type a number to see its square: "))
        
        # Calculate the square of the number
        square = number * number
        
        # Print the result in a formatted way
        print(f"{number} squared is {square}")
    
    except ValueError:
        # Handle the error if the user doesn't enter a valid number
        print("Please enter a valid number.")

if __name__ == '__main__':
    main()
