# Created as a part of the BAIL repository on 01/05 (technically 01/06 as its midnight...)

"""
Objective is to mimic the US lists game on https://www.sporcle.com/games/g/states
Using the turtle module, and the pandas module

TODO[]: Setup the screen and starting functions/attributes for the turtle
TODO[]: Read from the csv file and check users answer against all values in the file
TODO[]: If user answer matches the value in the file, the name should show up on the map
TODO[]:   - Keep a total correct/total count of states (out of 50) and have it update each time the user guesses correctly
"""

"""
HINTS PROVIDED BY THE CHALLENGE:
# 1: Convert to Title Case
# 2: Check if the guess is among the 50 states
# 3: Write correct guesses onto the map
# 4: Use a loop to allow the user to continue guessing
# 5: Record correct guesses in a list
# 6: Keep track of score
"""
###############


import pandas as pd
from turtle import Turtle, Screen, shape

image = "python_oop/US States/blank_states_img.gif"
screen = Screen()
screen.title("U.S States Game")
screen.addshape(image)

shape(image)
num_correct = 0

answer_state = screen.textinput(
    title="Guess the State", prompt="What's another states name?"
)
print(answer_state)
screen.mainloop()
