# Object States and Instances #

"""

We can make multiple turtles using the Turtle blueprint, and change their attributes individually.

timmy = Turtle()
tommy = Turtle()
jimmy = Turtle() and so on.

Each of these turtles represents an individual instance of the Turtle class.

This also means that each turtle could have different attributes and doing different things.
Ex) timmy could have its colour set to green, while tommy could be purple.

This concept is called an object state.
Ex)
timmy.colour = green
tommy.colour = purple

The next project will involve creating a turtle race to get familiar with object instances and object states.

"""

import random
from turtle import Turtle, Screen

# Initialize turtles
timmy = Turtle("turtle")
tommy = Turtle("turtle")
jimmy = Turtle("turtle")
jommy = Turtle("turtle")
tim = Turtle("turtle")
jom = Turtle("turtle")

# Initialize screen
screen = Screen()
screen.setup(width=500, height=400)

# List of turtle objects and their corresponding colors
turtles = [timmy, tommy, jimmy, jommy, tim, jom]
colours = ["red", "blue", "yellow", "green", "purple", "orange"]

# Starting positions
y_startingpoint = screen.canvheight / -2
x_startingpoint = screen.canvwidth / -2
colour_count = 0
screen_divisor = 0

# Starting grid #
for each_turtle in turtles:
    each_turtle.penup()  # Lift the pen to prevent drawing
    each_turtle.color(colours[colour_count])  # Set turtle color
    each_turtle.speed(10)  # Set turtle speed
    each_turtle.goto(
        x_startingpoint - 20, y_startingpoint + screen_divisor
    )  # Position turtle
    colour_count += 1
    screen_divisor += 60

# Prompt user for a bet
user_bet = screen.textinput(
    "Make your bet!", "Which colour will win the race? Type in a colour"
)

# Start race if user placed a bet
race_on = False
if user_bet:
    race_on = True

while race_on:

    for turtle in turtles:
        # Check if any turtle has reached the finish line
        if turtle.xcor() >= 230:
            race_on = False
            winning_colour = turtle.pencolor()

            # Announce race result
            if winning_colour == user_bet:
                print(f"You win! {winning_colour} won the race!")
            else:
                print(f"You lose. {winning_colour} turtle won")

        # Move turtle forward by a random distance
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()  # Close the screen when clicked
