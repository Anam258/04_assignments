# Useful constants to help make the math easier and cleaner!
DAYS_PER_YEAR: int = 365  # Number of days in a year
HOURS_PER_DAY: int = 24   # Number of hours in a day
MIN_PER_HOUR: int = 60    # Number of minutes in an hour
SEC_PER_MIN: int = 60     # Number of seconds in a minute

def main():
    """
    This function calculates and prints the total number of seconds in a year.
    It uses the provided constants for days, hours, minutes, and seconds.
    """
    
    # Calculate total seconds in a year using multiplication
    total_seconds = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    
    # Print the result in a nicely formatted way
    print(f"There are {total_seconds} seconds in a year!")

# Call the main function to execute the program
if __name__ == '__main__':
    main()
