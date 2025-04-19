# Password Generator - Python Project by Anam

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to the Random Password Generator!")

    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
        length = int(input("Enter the length of each password: "))

        print("\nHere are your passwords:")
        for i in range(num_passwords):
            print(f"{i + 1}: {generate_password(length)}")

    except ValueError:
        print("Please enter valid numbers only.")

# Run the password generator
main()
2
