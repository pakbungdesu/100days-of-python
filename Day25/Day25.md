
# 🗺️ U.S. States Quiz Game
An interactive educational game built with Python’s **Turtle** graphics and **Pandas**. Users guess state names to populate a map, while the program tracks progress and identifies areas for improvement.

## 🛠️ Features
**Interactive Map:** Uses a custom `.gif` background where state names appear at their exact geographical coordinates.

**Data-Driven Logic:** Utilizes Pandas to manage a database of 50 states, including their $(x, y)$ coordinates.

**Progress Tracking:** The window title updates dynamically to show the current score (e.g., "12/50 States Correct").

**Smart Export:** If the user quits early by typing "Exit," the game generates a `missing_states.csv` file for targeted study.

**Input Normalization:** Automatically formats user input (e.g., "ohio" to "Ohio") to ensure matches against the dataset.

## 🏗️ Project Structure
The project relies on a centralized script and external data files for a seamless experience:

**main.py:** The core logic handling the game loop, Turtle graphics rendering, and coordinate placement.

**50_states.csv:** The data source containing columns for `state`, `x`, and `y`.

**states_img.gif:** The visual map used as the game's interface.

## 🚀 How to Run
1. Ensure you have Python and the Pandas library installed:
```bash
pip install pandas
```

2. Place 50_states.csv and states_img.gif in the same directory as your script.
Run the program via your terminal:

```Bash
python main.py
```

## 🎮 How to Use
**Guessing:** Type the name of a U.S. state into the pop-up text box.

**Exit:** Type "Exit" to close the game and save a list of the states you missed.

**Win Condition:** Correctly identifying all 50 states triggers a "Congratulations" message and ends the game.

## ⚙️ Logic Workflow
**Coordinate Mapping:** When a correct guess is made, Pandas filters the CSV for that specific state's coordinates.

**Instant Rendering:** screen.tracer(0) and screen.update() are used to place text instantly without waiting for Turtle animations.

**State Persistence:** A unique list ensures users aren't rewarded for guessing the same state twice.

**Data Export:** Uses list comprehension to compare the master state list against user guesses to find the "remainder" for the study file.

## 👌🏼 Example Interaction

<img src="https://github.com/pakbungdesu/100days-of-python/blob/41b8777ebb1f3094a661281ef0d1ad595272836b/Day25/states.gif" alt="Demo" width="400" height="265">
<img src="https://github.com/pakbungdesu/100days-of-python/blob/41b8777ebb1f3094a661281ef0d1ad595272836b/Day25/winning.png" alt="Demo" width="400" height="265">