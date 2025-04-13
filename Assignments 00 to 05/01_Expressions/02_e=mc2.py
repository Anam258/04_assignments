"""
Program: e=mc^2
---------------------
This program demonstrates Einstein's famous equation, 
E = mc^2, where:
    E is the energy in joules,
    m is the mass in kilograms,
    c is the speed of light in meters per second.
The program takes the mass of an object as input and 
calculates the energy using the formula.
"""

C = 299792458  # Speed of light in meters per second (m/s)

def main():
    """
    The main function prompts the user to input a mass value in kilograms,
    calculates the energy in joules using the equation E = mc^2,
    and then prints the result.
    """
    # Prompt the user for the mass in kilograms
    mass_in_kg = float(input("Enter kilos of mass: "))

    # Calculate the energy in joules using the equation E = mc^2
    energy_in_joules = mass_in_kg * (C ** 2)

    # Print the results of the calculation
    print("e = m * C^2...")  # Formula representation
    print(f"m = {mass_in_kg} kg")  # Display the mass
    print(f"C = {C} m/s")  # Display the speed of light
    print(f"{energy_in_joules} joules of energy!")  # Display the calculated energy

# Ensure the main function is executed when the script is run
if __name__ == '__main__':
    main()
