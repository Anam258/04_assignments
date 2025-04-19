import hashlib

def hash_password(password):
    """
    Hashes the given password using SHA-256 and returns the hash in hexadecimal format.
    
    Args:
    - password (str): The password to be hashed.
    
    Returns:
    - str: The SHA-256 hash of the password.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    """
    Checks whether the provided email's stored password hash matches the hash of the input password.
    
    Args:
    - email (str): The email of the user trying to login.
    - password_to_check (str): The password entered by the user.
    - stored_logins (dict): A dictionary where the key is the email and the value is the hashed password.
    
    Returns:
    - bool: True if the login is successful (hashed password matches), False otherwise.
    """
    if email in stored_logins:  # Check if the email exists in stored logins
        stored_hash = stored_logins[email]  # Retrieve the stored password hash
        return stored_hash == hash_password(password_to_check)  # Compare the stored hash with the input password hash
    return False  # Return False if email is not found

def main():
    """
    Main function that handles user input and validates the login process.
    
    1. Collects email and password from user input.
    2. Checks if the email exists and the password is correct using the login function.
    3. Provides feedback to the user based on the login attempt.
    """
    # Example of stored logins with emails and their corresponding hashed passwords
    stored_logins = {
        "user@example.com": hash_password("securepassword123"),
        "anam@gmail.com": hash_password("myapple"),
    }

    # Collect user input for login credentials
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Check if the login is successful
    if login(email, password, stored_logins):
        print("Login successful! ✅")
    else:
        print("Login failed! ❌ Incorrect email or password.")  # Provide feedback if login fails

# This ensures the main function runs when the script is executed directly
if __name__ == '__main__':
    main()
