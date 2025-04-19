def main():
    # Dictionary to store gravity factors of each planet in the solar system
    planet_gravity = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    # Prompting the user to enter their weight on Earth
    earth_weight = float(input("Enter your weight on Earth (in kg): "))  # Convert to float for decimals
    planet = input("Enter the planet you want to know your weight on: ").capitalize()  # Capitalize input for uniformity

    # Checking if the entered planet is valid and calculating the weight
    if planet in planet_gravity:
        planet_weight = round(earth_weight * planet_gravity[planet], 2)  # Calculate weight on the specified planet
        print(f"Your weight on {planet}: {planet_weight} kg")  # Display result with two decimal places
    else:
        print("Invalid planet name. Please enter a valid planet from the solar system.")  # Error message for invalid input

# Ensuring main() runs when script is executed
if __name__ == "__main__":
    main()
