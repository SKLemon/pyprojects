# Created for BAIL repository on 01/12
import pandas as pd
from art import art

"""
NATO Alphabet Converter script:
To take any word the user types and outputs its NATO phonetic equivalent.
For Example:
User types:
VS Code

Program shows:
Victor, Sierra, Charlie, Oscar, Delta, Echo
"""
print(art)

# TODO: Create Dict in this format: {A:"Alpha", B: "Bravo"}.
# Convert CSV into a dictionary where the keys are letters and values are corresponding code words for those letters

nato_data = pd.read_csv("./nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

# TODO: Create a list of phonetic code words input by the user.
# I.E, User inputs "Hi", program spits out a list with ["Hotel", "India"]

while True:
    try:
        user_input = input("What is your input?: ").upper()
        converted_word = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print(f"Incorrect input. Try again with letters")
        continue
    else:
        print(converted_word)
        user_continue = input("More words? (Y/N)").lower()
    if user_continue == "n":
        break
