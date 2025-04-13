def main():
    # Assigning ages based on the given relationships
    Anton = 21          # Anton is 21 years old
    Beth = Anton + 6    # Beth is 6 years older than Anton
    Chen = Beth + 20    # Chen is 20 years older than Beth
    Drew = Anton + Chen # Drew is as old as Chen's age plus Anton's age
    Ethan = Chen        # Ethan is the same age as Chen

    # Printing the names and ages in the required format
    print(f"Anton is {Anton}")
    print(f"Beth is {Beth}")
    print(f"Chen is {Chen}")
    print(f"Drew is {Drew}")
    print(f"Ethan is {Ethan}")

if __name__ == '__main__':
    main()
