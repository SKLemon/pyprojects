import random
from turtle import Turtle, Screen

# import colorgram

# colours = colorgram.extract("image.jpg", 10) - Module to import, but NO LONGER NEEDED

tim = Turtle()
screen = Screen()
# screen.screensize(300,250) # To adjust the screen size if need be. Used in a different version, NO LONGER NEEDED
screen.colormode(255)


def random_colours():
    """
    Randomly generates colors in rgb format and appends to a list
    Return (list): Returns the list

    """
    colour_list = []

    """

    I was having issues in getting PIL and colorgram module to work in a headless env so the below is a function to randomly generate
    rbg values to use as colours for this project.

    """
    """

    UPDATE: Got DISPLAY var working so PIL and colorgram module can work now. Below function remains due to the simple fact that randomizing colours looks cooler

    """
    for i in range(1, 11):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        new_colour = r, b, g
        colour_list.append(new_colour)

    return colour_list


rgb_colours = random_colours()

"""
## Requirements of the painting

- Needs to be a 10 x 10 size painting - 10 x axis, 10 y axis
- Each dot is 20 in size, spaced by 50

"""


# dot_spacing = 50
#
# x_starting_point = dot_spacing - screen.canvwidth
# y_starting_point = dot_spacing - screen.canvheight
#
# tim.teleport(x_starting_point,y_starting_point)
#
# def dot_x():
#     x_new_dot = x_starting_point + dot_spacing
#     y_new_line = y_starting_point + dot_spacing
#     for dots in range(-250,250,50):
#
#         tim.teleport(x_new_dot,y_starting_point)
#         x_new_dot += dot_spacing
#### TODO: THE ABOVE CODE DOES NOT WORK. WILL EVENTUALLY FIND A FIX ###


#### THE BELOW CODE WAS WRITTEN BY https://www.udemy.com/user/marnus-van-wijk-2/ ####
### IT's too good not to use... ###

tim.penup()
tim.hideturtle()

for y in range(-250, 250, 50):
    for x in range(-250, 250, 50):
        tim.goto(x, y)
        tim.dot(20, random.choice(rgb_colours))

screen.exitonclick()