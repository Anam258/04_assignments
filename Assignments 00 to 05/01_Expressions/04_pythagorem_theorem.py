import math  # Importing the math module for square root calculation

def main():
    """
    This function prompts the user to input the lengths of sides AB and AC of a right triangle.
    It then calculates the length of the hypotenuse BC using the Pythagorean theorem:
    BC = sqrt(AB^2 + AC^2)
    Finally, it prints the result.
    """
    
    # Prompt the user to input the length of side AB
    ab = float(input("\033[1m\033[3mEnter the length of AB:\033[0m "))  
    
    # Prompt the user to input the length of side AC
    ac = float(input("\033[1m\033[3mEnter the length of AC:\033[0m "))  
    
    # Use the Pythagorean theorem to calculate the length of side BC
    bc = math.sqrt(ab**2 + ac**2)  
    
    # Output the calculated length of the hypotenuse BC
    print(f"The length of BC (the hypotenuse) is: {bc}")  

# Ensures that the main function is executed when the script is run
if __name__ == '__main__':
    main()
