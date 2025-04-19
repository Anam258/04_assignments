# Mad Libs Game - Python Project by Anam

# Collect input from the user
adjective = input("Enter an adjective (e.g., funny, scary): ")
animal = input("Enter the name of an animal: ")
verb = input("Enter a verb (e.g., run, jump): ")
exclamation = input("Enter an exclamation (e.g., Wow!, Oh no!): ")
sound = input("Enter a sound (e.g., roar, meow): ")

# Create the story using an f-string
story = f"""
One day, I went to the jungle and saw a {adjective} {animal}.
Suddenly, it started to {verb}!
I shouted, "{exclamation}"
Then the {animal} made a loud {sound} and ran away!
"""

# Display the story
print("\nHere’s your Mad Libs story:\n")
print(story)
