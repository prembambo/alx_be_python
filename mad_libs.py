# Ask the user for different types of words
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")

# Conditional twist
if animal.lower() == "cat":
    pet_comment = "a purring ball of fluff"
elif animal.lower() == "dog":
    pet_comment = "a loyal tail-wagging friend"
else:
    pet_comment = "a mysterious creature"

# Construct the story
story = (
    f"One day, I went to {place} and saw a very {adjective} {animal}.\n"
    f"I decided to {verb} it because it looked like {pet_comment}.\n"
    f"Suddenly, a {noun} fell from the sky and everyone laughed!"
)

# Print the final story
print("\nHere is your Mad Libs story:\n")
print(story)
