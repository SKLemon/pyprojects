# Made for BAIL repository on Github. Created 12/18

# TODO: Etch a Sketch App that abides by the following commands:
# W = move forwards
# S = move backwards
# A = counter clockwise
# D = clockwise
# C = clear drawings

from turtle import Turtle, Screen

# Create a turtle object named "tim"
tim = Turtle()

# Create a screen object to capture user input
screen = Screen()


# Define a function to move the turtle forward by 10 units
def move_forwards():
    tim.forward(10)


# Define a function to turn the turtle backwards by 10 units
def move_backwards():
    tim.backward(10)


# Define a function to turn the turtle counter clockwise by 5 units
def counter_clockwise():
    tim.left(5)


# Define a function to turn the turtle clockwise by 5 units
def clockwise():
    tim.right(5)


# Clears the screen and resets the turtle's position
def clear():
    tim.reset()


# Set up the screen to listen for key presses and bind them to keyboard
screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=counter_clockwise)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()
