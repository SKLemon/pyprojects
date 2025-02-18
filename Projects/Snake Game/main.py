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

SCREEN_REFRESH = 0.08

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    time.sleep(SCREEN_REFRESH)
    screen.update()
    snake.move()
    if snake.head.distance(food) < 15:
        food.new_location()
        snake.extend()
        scoreboard.increase_score()

screen.exitonclick()
