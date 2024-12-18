# Due to headless dev env and requirement of GUI for Turtle module, the rest of this code was created locally.
# The following is copy pasted as is from local env:

import turtle
from turtle import Turtle
from turtle import Screen
import random

tim = Turtle()

tim.color("blue2")
tim.shape("classic")

# Drawing a square #

# for i in range(4):
#     tim.forward(100)
#     tim.left(90)

# Importing modules

"""

We've already seen the basic import 'import'.
'from' import only imports the specific module and/or class being imported, but helps to avoid rewriting the module over and over again
For example: without 'from' import:
timmy = turtle.Turtle()
tommy = turtle.Turtle()
and so on.
timmy.forward(100)
Using 'from' allows me to rewrite just the class or item being imported, and saves typing and repetition
Another way is to use asteriks (*):
EX: from turtle import *
forward(100)

This is best avoided as it doesn't explain the source of where the blueprint/item or whatever came from.

BEST PRACTICE:
##### If you're using a module 3x or more, use 'from' import #####
##### Using it less? use 'import' #####

"""

# Aliasing Modules #

"""
You can import a module and rename it's import to something you prefer. For example:
import turtle as t
timmy = t.Turtle
"""

# Installing Modules #
"""
There only a handful of modules bundled with Python. The rest need to be installed using python packages.
Downloadable packages online. They get installed in a virtual env folder built in the python project

"""

# Drawing a dashed line #

# while tim.pos() != (100.00,0.00):
#     tim.pendown()
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)

# Drawing different shapes #

"""

The below is a more efficient and Pythonic

def create_shape(sides, length = 100):
    angle = 360 / sides
    for i in range(sides):
        tim.left(angle)
        tim.forward(length)

for sides in range(3,11):
    create_shape(sides)

"""

# # Below is functional and what I ended up making the first time around #

# def create_shape(shape_sides):
#     for i in range(shape_sides):
#         tim.left(360 / shape_sides)
#         tim.forward(100)
#
# tim_run = True
# shape_sides = 3
#
# while tim_run:
#     create_shape(shape_sides)
#     shape_sides += 1
#     if shape_sides > 10:
#         tim_run = False


# Drawing the random walk #

colour_palette = [
    "snow",
    "ghost white",
    "white smoke",
    "gainsboro",
    "floral white",
    "old lace",
    "linen",
    "antique white",
    "papaya whip",
    "blanched almond",
    "bisque",
    "peach puff",
    "navajo white",
    "lemon chiffon",
    "mint cream",
    "azure",
    "alice blue",
    "lavender",
    "lavender blush",
    "misty rose",
    "dark slate gray",
    "dim gray",
    "slate gray",
    "light slate gray",
    "gray",
    "light grey",
    "midnight blue",
    "navy",
    "cornflower blue",
    "dark slate blue",
    "slate blue",
    "medium slate blue",
    "light slate blue",
    "medium blue",
    "royal blue",
    "blue",
    "dodger blue",
    "deep sky blue",
    "sky blue",
    "light sky blue",
    "steel blue",
    "light steel blue",
    "light blue",
    "powder blue",
    "pale turquoise",
    "dark turquoise",
    "medium turquoise",
    "turquoise",
    "cyan",
    "light cyan",
    "cadet blue",
    "medium aquamarine",
    "aquamarine",
    "dark green",
    "dark olive green",
    "dark sea green",
    "sea green",
    "medium sea green",
    "light sea green",
    "pale green",
    "spring green",
    "lawn green",
    "medium spring green",
    "green yellow",
    "lime green",
    "yellow green",
    "forest green",
    "olive drab",
    "dark khaki",
    "khaki",
    "pale goldenrod",
    "light goldenrod yellow",
    "light yellow",
    "yellow",
    "gold",
    "light goldenrod",
    "goldenrod",
    "dark goldenrod",
    "rosy brown",
    "indian red",
    "saddle brown",
    "sandy brown",
    "dark salmon",
    "salmon",
    "light salmon",
]

# Increasing pen thickness and speed

tim.speed(10)
tim.width(10)
directions = [90, 180, 270, 360]

# Randomizing the walk of a turtle #


for i in range(0, 101):
    tim.forward(random.randint(10, 100))
    tim.setheading(random.choice(directions))
    tim.pencolor(random.choice(colour_palette))  # Randomizing the colour pallet

screen = Screen()
screen.exitonclick()
