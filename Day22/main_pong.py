"""
Pong Game - Main Controller
Coordinates paddle movement, ball physics, and score tracking.
"""

import time
from paddle_class import *
from ball_class import *
from score_class import *

# --- Screen Setup ---
# tracer(0) stops automatic animation so we can update it manually with screen.update()
screen.tracer(0)

# --- Object Initialization ---
# Create Left and Right paddles at specific screen coordinates
padL = Pad(370, 0)
padL.create_pad()
padR = Pad(-370, 0)
padR.create_pad()

# --- Controls ---
screen.listen()
# Player 1 (Right side of screen, using Arrow keys)
screen.onkey(padL.go_up, "Up")
screen.onkey(padL.go_down, "Down")
# Player 2 (Left side of screen, using WASD)
screen.onkey(padR.go_up, "w")
screen.onkey(padR.go_down, "s")

# Create the ball and the scoreboard
ball = Ball()
scoreboard = Score()

# --- Main Game Loop ---
game_on = True
while game_on:
    # Controls the speed of the game based on the ball's current move_speed
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # --- Wall Collision Logic ---
    # Detect if ball hits the top or bottom wall (approx 300 height)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_edge()

    # --- Paddle Collision Logic ---
    # distance() < 40: checks if the ball is close to the center of the paddle
    # xcor() checks: ensure the ball is actually at the horizontal position of the paddle
    if ball.distance(padL) < 40 and ball.xcor() > 340 or ball.distance(padR) < 40 and ball.xcor() < -340:
        ball.bounce_pad()

    # --- Score & Goal Logic ---
    # Ball goes past Left paddle (Right player scores)
    if ball.xcor() > 400:
        scoreboard.update_score("left")
        ball.move_speed = 0.1  # Reset speed for next round
        ball.setpos(0, 0)      # Reset ball position
        ball.bounce_pad()      # Launch ball towards the other player

    # Ball goes past Right paddle (Left player scores)
    if ball.xcor() < -400:
        scoreboard.update_score("right")
        ball.move_speed = 0.1
        ball.setpos(0, 0)
        ball.bounce_pad()

screen.exitonclick()