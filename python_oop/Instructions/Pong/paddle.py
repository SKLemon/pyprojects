""" This file contains the code for the paddle class. All attributes and methods, including the physics, the keys and button presses will be contained here """

from turtle import Turtle, mode


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.resizemode("user")
        self.shapesize(3, 1)
        self.goto(position)

    def up(self):
        up_y = self.ycor() + 20
        self.goto(self.xcor(), up_y) if self.ycor() < 265 else None

    def down(self):
        down_y = self.ycor() - 20
        self.goto(self.xcor(), down_y) if self.ycor() > -265 else None
