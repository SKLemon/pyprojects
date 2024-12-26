# Created for the BAIL repository on Github. Created 12/23/2024

# TODO: 1) Set up the screen
#           -
# TODO: 2) Create the paddles
#           - Create a second paddle for a 2-player game if need be (Ask the player how many players?)
#           -
# TODO: 3) Create the ball and make it move constantly
#           - Detect collisions with wall and when it should bounce
#           - Detect when misses occur
# TODO: 4) Create the scoreboard
#           - Track when misses occur and increase accordingly
#           - Game over when reaching a certain number?

"""
Pong Game Implementation using Python's Turtle Graphics Module
Players score points when the opponent misses the ball.
Paddles are tracked using keyboard keys (up or down)
Will need the screen set up, the ball and paddle physics, scoreboard to be calculated and added when scored on

"""
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

top_edge = screen.canvheight - 20
bottom_edge = -screen.canvheight + 20

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.update()
screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True

while game_on:
    if top_edge > ball.ycor() > bottom_edge:
        ball.move()
        screen.update()
        time.sleep(0.1)
    else:
        game_on = False
        screen.update()

screen.exitonclick()
