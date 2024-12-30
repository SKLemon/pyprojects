from turtle import Turtle
import random


class Food(Turtle):
    """Food Importing from turtle module and creating a class Food.

    Arguments:
        Turtle -- Turtle class from turtle module
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")  # Set the shape of the food to a circle
        self.penup()  # Lift the pen to avoid drawing lines
        self.shapesize(0.5, 0.5)  # Scale down the size of the food
        self.color("red")  # Set the color of the food to red
        self.speed("fastest")  # Set the speed of the food to the fastest
        self.new_location()  # Move the food to a new random location

    def new_location(self):
        """Move the food to a new random location on the screen."""
        self.goto(
            random.randint(-270, 277), random.randint(-270, 270)
        )  # Randomize the position
