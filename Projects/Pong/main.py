# Created for the BAIL repository on Github. Created 12/23/2024

# TODO: 1) Set up the screen
#           - Wider screen
#           - Tracer off
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
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create the paddles
r_paddle_edge = 330
l_paddle_edge = -330
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Create the ball
ball = Ball()

# Create the scoreboard
scoreboard = Scoreboard()

# Keyboard Bindings
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# Main game loop
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
        screen.update()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > r_paddle_edge:
        ball.bounce_paddle()
        screen.update()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.update_left()
        screen.update()

    # Detect collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < l_paddle_edge:
        ball.bounce_paddle()
        screen.update()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.update_right()
        screen.update()


screen.exitonclick()
