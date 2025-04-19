def main():
    """
    Main function to calculate the total cost of fruits based on user input.
    The program stores fruit prices in a dictionary and multiplies them by the
    quantity the user enters to calculate the total cost.
    """
    # Dictionary storing fruit prices (per unit)
    fruit_prices = {
        "apple": 3.5,
        "durian": 15.0,
        "jackfruit": 20.0,
        "kiwi": 2.5,
        "rambutan": 5.0,
        "mango": 7.0
    }

    total_cost = 0  # Initialize total cost to zero

    # Loop through each fruit and its price in the fruit_prices dictionary
    for fruit, price in fruit_prices.items():
        # Prompt the user to input the quantity of the current fruit
        quantity = int(input(f"How many {fruit}s do you want?: "))  # User input
        
        # Calculate the cost for the current fruit and add it to the total cost
        total_cost += quantity * price

    # Print the total cost, formatted to 2 decimal places
    print(f"\nYour total is: ${total_cost:.2f}")  # Display total cost

# This ensures that the main() function runs only when the script is executed directly
if __name__ == '__main__':
    main()
