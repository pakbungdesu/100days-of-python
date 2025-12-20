"""
Snake Game - Main Execution Script
This script handles the game loop, screen updates, and collision logic
between the snake, its food, and the wall.
"""

import time
from segment import Snake  # Assuming 'segment' contains the Snake class
from score import Score
from food import Food
from turtle import Screen

# --- Screen Setup ---
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turns off animation for smoother manual updates

# --- Object Initialization ---
game_on = True
food = Food()
snake = Snake()
scoreboard = Score()

# Initial snake setup
snake.create_snake()

# --- Main Game Loop ---
while game_on:
    # Update the screen manually every 0.1 seconds to show snake movement
    screen.update()
    time.sleep(0.1)

    snake.movement()
    snake.control()

    # Detect collision with wall (Screen is 600x600, range is -300 to 300)
    # Using 325 allows a small buffer, but 280-290 is safer for strict walls
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        scoreboard.game_over()
        game_on = False

    # Detect collision with food
    # distance() measures from center to center; 17-20 pixels is the standard hit box
    if snake.head.distance(food) < 17:
        food.refresh_food()
        scoreboard.refresh_score()
        snake.add_snake()

    # Detect collision with tail
    # Slicing [1:] ensures we don't check the head against itself
    for segment in snake.parts[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_on = False

# Keeps the window open until the user clicks
screen.exitonclick()
