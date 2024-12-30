# Created as a part of BAIL repository on github. Created 12/19

# Requirements and Progress:
# ✓ Create a snake body [DONE]
#   - Created 3 squares on screen
#   - Implemented basic movement
# ✓ Move the snake [DONE]
#   - Basic forward movement implemented
#   - Segment following system working
# ✓ Control the snake [DONE]
#   - Implement keyboard controls for direction
# ✓ Detect collision with food [DONE]
#   - Create food at random points
#   - Handle collision detection
# ✓ Create a scoreboard [DONE]
#   - Add score display
#   - Update score on food collision

# Remaining TODOs:
# 4. Detect collision with wall
#   - Add wall boundaries
#   - Implement game over on wall collision
# 5. Detect collision with tail
#   - Add self-collision detection
#   - Implement game over on tail collision

import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SCREEN_REFRESH = 0.05

screen = Screen()
screen.setup(width=600, height=600)  # Set up the screen size
screen.bgcolor("black")  # Set the background color to black
screen.title("Snake Game")  # Set the window title
screen.tracer(0)  # Turn off automatic screen updates

X_EDGE = screen.canvwidth - 90  # Define the horizontal boundary
Y_EDGE = screen.canvheight - 10  # Define the vertical boundary

snake = Snake()  # Create a snake object
food = Food()  # Create a food object
scoreboard = Scoreboard()  # Create a scoreboard object

screen.listen()  # Listen for keyboard input
screen.onkey(snake.up, "Up")  # Bind the up arrow key to the snake's up method
screen.onkey(snake.down, "Down")  # Bind the down arrow key to the snake's down method
screen.onkey(snake.left, "Left")  # Bind the left arrow key to the snake's left method
screen.onkey(
    snake.right, "Right"
)  # Bind the right arrow key to the snake's right method

game_on = True
while game_on:
    time.sleep(SCREEN_REFRESH)  # Pause the game for a short period
    screen.update()  # Update the screen
    snake.move()  # Move the snake

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.new_location()  # Move the food to a new location
        snake.extend()  # Extend the snake
        scoreboard.increase_score()  # Increase the score

    # Detect collision with wall
    if (
        snake.head.xcor() > X_EDGE
        or snake.head.xcor() < -X_EDGE
        or snake.head.ycor() > Y_EDGE
        or snake.head.ycor() < -Y_EDGE
    ):
        game_on = False  # End the game
        scoreboard.clear()  # Clear the scoreboard
        scoreboard.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False  # End the game
            scoreboard.clear()  # Clear the scoreboard
            scoreboard.reset()

screen.exitonclick()  # Exit the game when the screen is clicked
