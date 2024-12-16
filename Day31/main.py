from tkinter import *
import pandas as pd

# -------------------- CONSTANT ------------------- #

WHITE = "#FFFFFF"
BLACK = "#000000"
BACKGROUND_COLOR = "#B1DDC6"
HEADING_FONT = ("Ariel", 35, "italic")
WORD_FONT = ("Ariel", 45, "bold")
timer = None
idx = 0
current_word = {}
my_word = {}

# -------------------- CSV ------------------- #

try:
    df = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("original_words.csv")
    my_word = df.to_dict(orient="records")
else:
    my_word = df.to_dict(orient="records")


# -------------------- FUNCTION ------------------- #


def know_check():
    global idx
    my_word.pop(idx)  # Remove the current word from the list
    new_df = pd.DataFrame(my_word)
    new_df.to_csv("words_to_learn.csv", index=False)
    change_word(idx)


def unknown_check():
    global idx
    idx += 1
    change_word(idx)


def change_word(i):
    global idx, current_word
    idx = i
    if i < len(my_word):
        current_word = my_word[i]

        # front
        canvas.itemconfig(heading, text="Japanese")
        canvas.itemconfig(word, text=current_word["Japanese"])
        canvas.itemconfig(flashcard, image=front_image)

        # back
        window.after(5000, lambda: canvas.itemconfig(heading, text="English"))
        window.after(5000, lambda: canvas.itemconfig(word, text=current_word["English"]))
        window.after(5000, lambda: canvas.itemconfig(flashcard, image=back_image))


# -------------------- UI SETUP ------------------- #


# Window
window = Tk()
window.title("My Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
flashcard = canvas.create_image(400, 263, image=front_image)
heading = canvas.create_text(400, 150, text="Japanese", fill=BLACK, font=HEADING_FONT)
word = canvas.create_text(400, 263, text="会う, あう", fill=BLACK, font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)
change_word(0)  # call function to change word every 5 seconds

# Button
know_img = PhotoImage(file="images/right.png")
know_button = Button(image=know_img, highlightthickness=0, command=know_check)
know_button.grid(row=1, column=1)

unknown_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_img, highlightthickness=0, command=unknown_check)
unknown_button.grid(row=1, column=0)

window.mainloop()
