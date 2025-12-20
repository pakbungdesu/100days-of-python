"""
Pomodoro Timer Application
A productivity tool using the Pomodoro technique (25m work / 5m break).
Uses Tkinter for the GUI and recursive function calls for the timer logic.
"""

from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
# Color Palette & Timing settings
RED = "#EB455F"
BLUE = "#16325B"
YELLOW = "#FFDC7F"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    """
    Stops the active timer, resets the display to 00:00,
    and clears all progress checkmarks.
    """
    global timer
    global reps
    window.after_cancel(timer)  # Stops the scheduled .after() event
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=YELLOW)
    check_marks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    """
    Determines whether the user should be working or taking a break
    based on the current repetition count.
    """
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Logic: 8th rep = Long Break, even reps = Short Break, odd reps = Work
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=YELLOW)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    """
    Updates the UI every second to reflect the remaining time.
    Uses window.after() for non-blocking recursion.

    Args:
        count (int): Total seconds remaining in the current session.
    """
    count_min = floor(count / 60)
    count_sec = count % 60

    # Dynamic Typing: Formatting seconds to always show two digits (e.g., 05 instead of 5)
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        # schedule count_down to be called again after 1000ms (1 second)
        timer = window.after(1000, count_down, count - 1)
    else:
        # Session ended: Start next session and update checkmarks
        start_timer()
        marks = ""
        work_sessions = floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

# Initialize main window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=80, pady=40, background=BLUE)

# Title Label (Timer / Work / Break)
title_label = Label(text="Timer", fg=YELLOW, bg=BLUE, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

# Main Canvas for Tomato Image and Digital Timer
canvas = Canvas(width=200, height=224, background=BLUE, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(110, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=2)

# Control Buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=4)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=4)

# Checkmark display to track completed work sessions
check_marks = Label(fg=YELLOW, bg=BLUE, font=(FONT_NAME, 15))
check_marks.grid(column=1, row=4)

window.mainloop()
