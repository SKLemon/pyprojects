""" This file contains the code for the ball class"""

from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.resizemode("user")
        self.shapesize(1, 1)
        self.color("white")

    def move(self):
        new_x = self.xcor() + 15
        new_y = self.ycor() + 15
        self.goto(new_x, new_y)
