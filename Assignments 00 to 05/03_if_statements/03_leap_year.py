# Program to determine whether a given year is a leap year or not

def determine_leap_year():
    # Ask the user to enter a year
    input_year = int(input("Enter a year: "))

    # Apply leap year logic based on Gregorian calendar rules
    if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

# Start of the program
if __name__ == '__main__':
    determine_leap_year()
