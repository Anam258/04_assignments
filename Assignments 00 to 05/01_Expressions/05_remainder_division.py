def main():
    """
    This function prompts the user to input two integers.
    It then calculates the quotient (integer division) and the remainder of dividing
    the first number by the second number using the floor division (//) and modulo (%) operators.
    Finally, it prints the result.
    """
    
    # Prompt user to input the first integer (to be divided)
    num1: int = int(input("\033[1;3mPlease enter an integer to be divided:\033[0m "))  
    
    # Prompt user to input the second integer (the divisor)
    num2: int = int(input("\033[1;3mPlease enter an integer to divide by:\033[0m "))  

    # Calculate the quotient using floor division (//)
    quotient: int = num1 // num2
    
    # Calculate the remainder using modulo (%)
    remainder: int = num1 % num2

    # Output the result: quotient and remainder
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

# This line ensures that the main function is called when the script is executed
if __name__ == '__main__':
    main()
