# Program to check voting eligibility for three fictional countries with different age requirements

def check_voting_eligibility():
    # Ask the user to input their age
    user_age = int(input("How old are you? "))

    # Check eligibility for Peturksbouipo (Voting age: 16)
    if user_age >= 16:
        print("You can vote in Peturksbouipo where the voting age is 16.")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16.")

    # Check eligibility for Stanlau (Voting age: 25)
    if user_age >= 25:
        print("You can vote in Stanlau where the voting age is 25.")
    else:
        print("You cannot vote in Stanlau where the voting age is 25.")

    # Check eligibility for Mayengua (Voting age: 48)
    if user_age >= 48:
        print("You can vote in Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in Mayengua where the voting age is 48.")

# Program execution starts here
if __name__ == '__main__':
    check_voting_eligibility()
