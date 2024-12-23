from turtle import Turtle
import random


class Food(Turtle):
    """Food Importing from turtle module and creating a class Food.

    Arguments:
        Turtle -- Turtle class from turtle module
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.new_location()

    def new_location(self):
        self.goto(random.randint(-270, 277), random.randint(-270, 270))
