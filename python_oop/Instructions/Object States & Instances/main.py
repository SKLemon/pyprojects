# Object States and Instances #

"""

We can make one turtle using Turtle blueprint. We can also make more using the same blueprint, and change its attributes.
timmy = Turtle()
tommy = Turtle()
jimmy = Turtle() and so on.

Each of these turtles represents an individual instance of the Turtle class.

This also means that each turtle could have different attributes and doing different things.
Ex) timmy could have its colour set to green, while tommy could be purple.
This fact is called an object state... Like the state of an object.
Ex)
timmy.colour = green
tommy.colour = purple

The next project will be creating a turtle race to get familiar with the object instances and object states.

"""

import random
from turtle import Turtle, Screen

# Initialize turtles and screen
timmy = Turtle("turtle")
tommy = Turtle("turtle")
jimmy = Turtle("turtle")
jommy = Turtle("turtle")
tim = Turtle("turtle")
jom = Turtle("turtle")

screen = Screen()
screen.setup(width=500, height=400)

turtles = [timmy, tommy, jimmy, jommy, tim, jom]
colours = ["red", "blue", "yellow", "green", "purple", "orange"]

y_startingpoint = screen.canvheight / -2
x_startingpoint = screen.canvwidth / -2
colour_count = 0
screen_divisor = 0

# Starting grid #
for each_turtle in turtles:
    each_turtle.penup()
    each_turtle.color(colours[colour_count])
    each_turtle.speed(10)
    each_turtle.goto(x_startingpoint - 20, y_startingpoint + screen_divisor)
    colour_count += 1
    screen_divisor += 60

user_bet = screen.textinput(
    "Make your bet!", "Which colour will win the race? Type in a colour"
)

race_on = False
if user_bet:
    race_on = True

while race_on:

    for turtle in turtles:

        if turtle.xcor() >= 230:
            race_on = False
            winning_colour = turtle.pencolor()

            if winning_colour == user_bet:
                print(f"You win! {winning_colour} won the race!")
            else:
                print(f"You lose. {winning_colour} turtle won")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()