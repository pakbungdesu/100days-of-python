"""
Flashy: A Language Learning Application
Uses spaced repetition by tracking which words the user has mastered.
Features include a flipping card mechanism and CSV data persistence.
"""

from tkinter import *
import pandas as pd

# -------------------- CONSTANTS ------------------- #
WHITE = "#FFFFFF"
BLACK = "#000000"
BACKGROUND_COLOR = "#B1DDC6"
HEADING_FONT = ("Ariel", 35, "italic")
WORD_FONT = ("Ariel", 45, "bold")
FLIP_DELAY = 5000  # Time in milliseconds before the card flips

# Global variables for tracking the session
timer = None
idx = 0
current_word = {}
my_word = {}

# -------------------- DATA LOADING ------------------- #

# Attempt to load progress from 'words_to_learn.csv'.
# If it doesn't exist, load the full 'original_words.csv' dictionary.
try:
    df = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("original_words.csv")
    # 'records' orientation creates a list of dictionaries: [{'Japanese': '...', 'English': '...'}, ...]
    my_word = df.to_dict(orient="records")
else:
    my_word = df.to_dict(orient="records")


# -------------------- FUNCTIONS ------------------- #

def know_check():
    """
    Called when user clicks the 'Check' button.
    Removes the current word from the study list and saves progress.
    """
    global idx
    if len(my_word) > 0:
        my_word.pop(idx)  # Remove the mastered word
        # Create a new CSV without the known word to update progress
        new_df = pd.DataFrame(my_word)
        new_df.to_csv("words_to_learn.csv", index=False)
        change_word(idx)


def unknown_check():
    """
    Called when user clicks the 'X' button.
    Moves to the next word without removing the current one from the list.
    """
    global idx
    idx += 1
    change_word(idx)


def change_word(i):
    """
    Updates the UI with a new Japanese word and schedules the card flip.

    Args:
        i (int): The index of the word to display in the my_word list.
    """
    global idx, current_word
    idx = i

    # Check if we still have words left to study
    if i < len(my_word):
        current_word = my_word[i]

        # Reset card to 'Front' (Japanese side)
        canvas.itemconfig(heading, text="Japanese", fill=BLACK)
        canvas.itemconfig(word, text=current_word["Japanese"], fill=BLACK)
        canvas.itemconfig(flashcard, image=front_image)

        # Schedule the flip to 'Back' (English side) after a delay
        # Lambda is used here to execute multiple configuration changes after the timer
        window.after(FLIP_DELAY, lambda: flip_card())


def flip_card():
    """Updates the canvas to show the English translation and back-side image."""
    canvas.itemconfig(heading, text="English", fill=WHITE)
    canvas.itemconfig(word, text=current_word["English"], fill=WHITE)
    canvas.itemconfig(flashcard, image=back_image)


# -------------------- UI SETUP ------------------- #

window = Tk()
window.title("My Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Main Display Area
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

flashcard = canvas.create_image(400, 263, image=front_image)
heading = canvas.create_text(400, 150, text="", font=HEADING_FONT)
word = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Control Buttons
know_img = PhotoImage(file="images/right.png")
know_button = Button(image=know_img, highlightthickness=0, command=know_check)
know_button.grid(row=1, column=1)

unknown_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_img, highlightthickness=0, command=unknown_check)
unknown_button.grid(row=1, column=0)

# Load the first word
change_word(0)

window.mainloop()
