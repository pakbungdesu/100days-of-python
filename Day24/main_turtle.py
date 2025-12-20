"""
Turtle Crossing - Main Game Loop
Handles screen updates, player movement, car spawning, collision detection,
and level transitions.
"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# --- Constants ---
FINISH_LINE = 280

# --- Screen Setup ---
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Smooth animation by turning off automatic screen updates

# --- Object Initialization ---
turtle = Player()
cars = CarManager()
scores = Scoreboard()

# --- Controls ---
screen.listen()
screen.onkey(turtle.move_forward, "Up")

# --- Game State ---
level = 1
scores.write_score(level)
game_on = True
increment = 0  # Additional speed added to cars as levels increase

# --- Main Game Loop ---
while game_on:
    # Set the frame rate (0.1 seconds per frame)
    time.sleep(0.1)
    screen.update()

    # Manage traffic
    cars.create_car()
    cars.car_move(increment)

    # --- Level Up Logic ---
    # Detect if the player reached the top finish line
    if turtle.ycor() > FINISH_LINE:
        increment += 2     # Make cars faster for the next level
        turtle.back_home() # Reset player position
        level += 1
        scores.write_score(level)

    # --- Collision Detection ---
    # Check distance between the player and every car in the list
    for car in cars.all_cars:
        # 20 pixels is the standard 'hitbox' for a square/rectangle Turtle collision
        if turtle.distance(car) < 20:
            game_on = False

# --- Game End ---
scores.write_game_over()
screen.exitonclick()
