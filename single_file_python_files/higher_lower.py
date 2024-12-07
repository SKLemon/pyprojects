


# Logo imports
import random
from art import logo_higherlower, vs_higherlower
from game_data import data
print(logo_higherlower)

# Comparison line print statement
# Importing the data and randomizing the choice
comparison_A = random.choice(data) #only runs once when game starts, then gets overidden everytime if user_answer is correct
print(f"Compare A: {comparison_A["name"]}, a {comparison_A["description"]}, from {comparison_A["country"]}")


while True:
    comparison_B = random.choice(data)
    print(vs_higherlower)
    print(f"Compare B: {comparison_B["name"]}, a {comparison_B["description"]}, from {comparison_B["country"]}")
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    break
# User choice and way to keep track of score
# Score does not empty until the game is ended. Does not repeat automatically once game is ended

# Seems the user's previous choice gets pulled into comparison A.
# Only on the first run does the first comparison list get randomly chosen... comparison_b gets randomly chosen everytime

