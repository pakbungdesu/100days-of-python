
# 🏓 Classic Pong Game (OOP Edition)
A smooth, two-player Pong game built with Python's turtle graphics. This project focuses on collision physics, animation control, and dynamic speed scaling.

## 🚀 Features
**Dynamic Speed:** The ball speeds up every time it hits a paddle, increasing the difficulty as the rally continues.

**Physics Logic:** Handles vertical wall bouncing and horizontal paddle deflection.

**Dual Score Tracking:** Independent scoreboards for both left and right players.

**Custom Animations:** Uses screen.tracer(0) for lag-free, high-performance movement.

## 🏗 Game Architecture

The project is built using four main components:

**Ball Class:** Manages (x, y) movement vectors.Logic for bounce_edge (top/bottom) and bounce_pad (left/right).Speed management using move_speed.

**Pad Class:** Creates the rectangular paddles using coordinate stretching (shapesize).Handles vertical movement with boundary control.

**Score Class:** Utilizes the ```.write()``` method to render high-fidelity text.Tracks and updates l_score and ```r_score.process()``` 

**Engine:** The main game loop that coordinates movement, collision detection, and scoring events.

## 🎮 Controls
The game is designed for Local Multiplayer:

|Action|Left Player|Right Player|
| ------------- | ------------- | ------------- |
Move Up|W Key|Up Arrow
Move Down|S Key|Down Arrow

## 🛠 Technical Highlights
Collision Detection
The game uses the Pythagorean distance formula (via ```ball.distance()```) combined with x-coordinate checks to ensure the ball only bounces when hitting the face of the paddle:

```Python
if ball.distance(padL) < 40 and ball.xcor() > 340:
    ball.bounce_pad()
```

**Reset Logic**
When a player scores, the ball resets to the center and its speed is restored to the default value, but the direction is flipped so the losing player receives the next serve.

## 📝 Setup & Installation
Clone the repository.

Ensure Python is installed. (Standard library turtle and time are required).

Run the game:

```commandline
cd Day22
python main.py
```

## 👌🏼 Example Interaction

