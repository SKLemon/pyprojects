""" This file contains the code for the ball class"""

from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.resizemode("user")
        self.shapesize(1, 1)
        self.color("white")
        self.x_distance = 15
        self.y_distance = 15

    def move(self):
        new_x = self.xcor() + self.x_distance
        new_y = self.ycor() + self.y_distance
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_distance *= -1

    def bounce_paddle(self):
        self.x_distance *= -1
