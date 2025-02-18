# Created as a part of the BAIL repository on Github. Created 12/05/2024

import random
from art import logo_higherlower, vs_higherlower as vs
from game_data import data

print(logo_higherlower)  # ASCII art

# After review, this does not adhere to DRY principle if there are multiple data sets later on. Ex multiple lines of data_c and so forth.

# To make this efficient for re-useability later on:
# 1) define a helper function that converts the dictionary entries into seperate variables
# 2) Use an f string to return individual variables formatted how you prefer.

# Example below:
#
# def format_data(dataset):
#     dataset_name = dataset["name"]
#     dataset_descr = dataset["description"]
#     dataset_country = dataset["country"]
#     return f"{dataset_name}, a {dataset_descr}, from, {dataset_country}."

# Then when you need to call your statement

# print(f"Compare A: {format_data(comparison_A)}")
# print(f"Compare B: {format_data(comparison_B)}")


def comparison(
    data_a,
    data_b,
):
    """data_a: Data set 1 to compare.\n
    data_b: Data set 2 to compare.\n
    This function prints out the name, description, and country from the dict in (data)
    """

    print(
        f"Compare A: {data_a['name']}, a {data_a['description']}, from {data_a['country']}"
    )
    print(vs)
    print(
        f"Compare B: {data_b['name']}, a {data_b['description']}, from {data_b['country']}"
    )


def correct_randomizer(data_a, data_b, data):
    """Checks comparison() data sets and rewrites the first one (data_a) on a correct answer, while randomizing the second dataset (data_b)"""

    data_a = data_b
    data_b = random.choice(data)
    return data_a, data_b


# First run - every comparison option is randomized and zeroed the score
user_score = 0
comparison_A = random.choice(data)
comparison_B = random.choice(data)
game_win = True

comparison(comparison_A, comparison_B)  # First run print. Both data_sets are randomized

while game_win == True:
    # This sets the correct answer by checking whcih data set has the higher follower count
    if comparison_A["follower_count"] > comparison_B["follower_count"]:  # type: ignore
        correct_answer = "a"
    else:
        correct_answer = "b"

    user_guess = input(
        "Who has more followers? Type 'A' or 'B': "
    ).lower()  # user input stored into a var
    print("\n" * 20)
    print(logo_higherlower)

    # Below is game winning criteria.
    if user_guess != correct_answer:
        game_win = False
        print(f"Sorry, that's wrong. Final Score: {user_score}")

    else:
        user_score += 1
        print(f"You're right! Current score: {user_score}\n")
        comparison_A, comparison_B = correct_randomizer(
            comparison_A, comparison_B, data
        )
        comparison(comparison_A, comparison_B)
