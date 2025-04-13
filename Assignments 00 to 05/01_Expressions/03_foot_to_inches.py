"""
Program: foot_to_inches
------------------------
This program converts a given length in feet to inches.
1 foot is equal to 12 inches, so the program multiplies 
the number of feet by 12 to calculate the equivalent length in inches.
"""

INCHES_IN_FOOT = 12  # Constant representing the number of inches in one foot

def main():
    """
    The main function prompts the user to input a length in feet,
    calculates the equivalent length in inches, and then prints the result.
    """
    # Prompt the user to enter the number of feet
    feet = float(input("Enter number of feet: "))  

    # Convert the feet to inches by multiplying by the constant INCHES_IN_FOOT
    inches = feet * INCHES_IN_FOOT  

    # Output the equivalent length in inches
    print(f"That is {inches} inches!")

# Ensure the main function is executed when the script is run
if __name__ == '__main__':
    main()
