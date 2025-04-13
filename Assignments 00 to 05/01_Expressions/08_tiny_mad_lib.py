# Sentence beginning
SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my "

def main():
    """
    This function prompts the user to enter an adjective, a noun, and a verb, 
    and then constructs and prints a fun sentence using those inputs.
    """
    
    # Get the three inputs from the user
    adjective: str = input("Please type an adjective and press enter. ")  # User enters an adjective
    noun: str = input("Please type a noun and press enter. ")  # User enters a noun
    verb: str = input("Please type a verb and press enter. ")  # User enters a verb

    # Combine the inputs with the sentence start to form a fun sentence
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")  # Print the final sentence

# Call the main function to run the program
if __name__ == '__main__':
    main()
