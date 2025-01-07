# Created as a part of the BAIL repository on 01/05 (technically 01/06 as its midnight...)

"""
Objective is to mimic the US lists game on https://www.sporcle.com/games/g/states
Using the turtle module, and the pandas module

TODO[✔]: Setup the screen and starting functions/attributes for the turtle
TODO[✔]: Read from the csv file and check users answer against all values in the file
TODO[✔]: If user answer matches the value in the file, the name should show up on the map
TODO[✔]:   - Keep a total correct/total count of states (out of 50) and have it update each time the user guesses correctly
"""

"""
HINTS PROVIDED BY THE CHALLENGE:
# 1: Convert to Title Case ✔
# 2: Check if the guess is among the 50 states ✔
# 3: Write correct guesses onto the map ✔
# 4: Use a loop to allow the user to continue guessing ✔
# 5: Record correct guesses in a list ✔
# 6: Keep track of score ✔
"""
###############


import pandas as pd
from turtle import Turtle, Screen

# Setting initial var
turtle = Turtle()
screen = Screen()
screen.title("U.S States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

## Reading the csv file and converting to DataFrame
data = pd.read_csv("./50_states.csv")

# Turning States column into a list for iteration
states_list = data["state"].to_list()

# Starting variables
t = Turtle()
t.penup()
t.hideturtle()
correct_guesses = []

# Main game loop
while len(correct_guesses) < len(states_list):
    answer_state = screen.textinput(
        title=f"Guess another: {len(correct_guesses)} / {len(states_list)}",
        prompt="What is the name of a State?",
    ).title()

    # Conditional to check if complete or to continue
    if answer_state in states_list and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        state_coords = data[data.state == answer_state]
        t.goto(state_coords.x.item(), state_coords.y.item())
        t.write(answer_state)
        t.home()

    if answer_state == "Exit":
        missing_states = []
        for each_state in states_list:
            if each_state not in correct_guesses:
                missing_states.append(each_state)
        pd.DataFrame(missing_states).to_csv(
            "/home/snowyp/repos/pyprojects/python_oop/US States/states_to_learn.csv"
        )
        break

screen.exitonclick()
