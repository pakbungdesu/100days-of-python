
# 🐢 Turtle Crossing: Traffic Dodge
A fast-paced arcade game built with Python's turtle module. 

The goal is simple: get the turtle across the busy road to the finish line without getting hit by colorful, speeding cars.

## 🚀 Features
**Infinite Leveling:** Every time you reach the finish line, the level increases and the cars move faster.

**Procedural Traffic:** Cars are spawned at random intervals and in random "lanes" to ensure no two games are the same.

**Collision Physics:** Precise hitbox detection between the player and the car objects.

**Score Persistence:** Real-time level tracking displayed via a top-left HUD.

## 🏗 Game Architecture
The project follows a modular OOP structure, separating the player, the traffic, and the game logic:

**Player Class:** Handles the turtle's upward movement. Logic for resetting to the back_home() starting position upon success or failure.

**CarManager Class:** A "Factory" class that manages a list of traffic objects. Uses randrange to control car density and lane assignment. Handles the increment logic to increase speed as the levels progress.

**Scoreboard Class:** A dedicated UI controller for the Level counter and the "GAME OVER" splash screen.

**process.py (Game Engine):** Coordinates the screen refresh rates (tracer logic). Listens for keyboard events and checks for collision overlap

## 🎮 How to Play
Run the game:

```Bash
python main.py
```

**Controls:** Press the Up Arrow key to move forward.

**Goal:** Reach the top of the screen (y > 280) to advance to the next level.

**Lose Condition:** If any part of the turtle touches a car, the game ends immediately.

## 🛠 Technical Highlights
**Dynamic Speed Increment**
Instead of static movement, the game uses a variable increment passed to the car manager. This allows for a smooth difficulty curve:

```Python
if turtle.ycor() > FINISH_LINE:
    increment += 2  # Increases speed by 20% of base DISTANCE
```

**The "1-in-6" Spawn Rate**
To prevent the screen from being flooded with too many cars, a probability check is performed every frame (approx. 10 times per second):

```Python
rand_n = rand.randrange(1, 7)
if rand_n == 1:
    # Create new car...
```

## 👌🏼 Example Interaction
![Turtle Crossing Demo](./turtle_game.gif)
