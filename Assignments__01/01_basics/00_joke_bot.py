# Constants to store predefined messages
REQUEST_PROMPT = "What would you like to hear?"
PROGRAM_JOKE = "Here's a fun one for you! Panaversity GPT - Sophia heads out to the grocery store. A programmer tells her: 'Pick up a liter of milk, and if they have eggs, grab 12.' Sophia comes back with 13 liters of milk. When asked why, she responds: 'Because they had eggs.'"
APOLOGY_MESSAGE = "Apologies, I only tell jokes."

def main():
    # Prompting the user for input
    user_response = input(REQUEST_PROMPT)
    
    # Checking the user's response
    if user_response.lower() == "joke":  # If the user asks for a joke (case-insensitive)
        print(PROGRAM_JOKE)  # Output the joke
    else:
        print(APOLOGY_MESSAGE)  # Output the apology message

# Ensures the main function is called when the script runs
if __name__ == '__main__':
    main()
