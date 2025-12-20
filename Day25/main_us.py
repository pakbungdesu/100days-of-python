"""
U.S. States Quiz Game
An interactive map game that uses Pandas for data handling and Turtle
for graphical feedback. Tracks user progress and exports missing states.
"""

import turtle as t
import pandas as pd

# --- Screen & Background Setup ---
screen = t.Screen()
screen.title("U.S. States Game")
screen.setup(800, 500)
image = "states_img.gif"
screen.bgpic(image)  # Sets the map image as the background
screen.tracer(0)  # Disables animation for instant text placement

# --- Turtle Configuration ---
# Use the root turtle for writing state names on the map
t.hideturtle()
t.penup()

# --- Data Handling with Pandas ---
df = pd.read_csv("50_states.csv")
# Convert the 'state' column into a list for easy lookup
states = df["state"].to_list()

# --- Game State ---
unique = []  # List to track correctly guessed states

while True:
    # Prompt user for input and display current score in the title bar
    answer = screen.textinput(f"{len(unique)}/50 States Correct", "What's another state's name?")

    # Handle Cancel button or empty input
    if answer is None:
        break

    answer = answer.title()  # Formats input (e.g., 'ohio' -> 'Ohio')

    # --- Exit & Save Logic ---
    if answer == "Exit":
        # List Comprehension: find states that were NOT guessed
        learn_more = [ele for ele in states if ele not in unique]
        # Export missing states to a new CSV for the user to study
        pd.DataFrame(learn_more).to_csv("missing_states.csv", index=False)
        break

    # --- Correct Guess Logic ---
    if answer in states and answer not in unique:
        unique.append(answer)
        # Filter the DataFrame to find the specific state's coordinates
        correct = df[df.state == answer]

        # item() extracts the raw value from the Pandas series
        t.setpos(correct.x.item(), correct.y.item())
        t.write(answer, False, "center", ('Arial', 8, 'normal'))
        screen.update()  # Refresh screen to show the new text

    # --- Win Condition ---
    if len(unique) == 50:
        t.goto(0, 0)
        t.write("Congratulations! You know all 50 states!", align="center", font=("Arial", 20, "bold"))
        break

screen.exitonclick()
