# Made for BAIL repository on Github. Created 12/18

# TODO: Etch a Sketch App that abides by the following commands:
# W = move forwards
# S = move backwards
# A = counter clockwise
# D = clockwise
# C = clear drawings

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def counter_clockwise():
    tim.left(5)


def clockwise():
    tim.right(5)


def clear():
    tim.reset()


screen.onkeypress(key="w", fun=move_forwards)

screen.onkeypress(key="s", fun=move_backwards)

screen.onkeypress(key="a", fun=counter_clockwise)

screen.onkeypress(key="d", fun=clockwise)

screen.onkeypress(key="c", fun=clear)

screen.listen()
screen.exitonclick()
