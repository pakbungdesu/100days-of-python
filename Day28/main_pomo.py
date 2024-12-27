
from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #

RED = "#EB455F"
BLUE = "#16325B"
YELLOW = "#FFDC7F"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global title_label
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break")
    else:
        count_down(work_sec)
        title_label.config(text="Work")


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global timer
    window.after_cancel(timer)  # cancel the ongoing timer
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(minute):
    count_min = floor(minute / 60)
    count_sec = minute % 60
    if count_sec in range(10):
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if minute > 0:
        # return timer
        global timer
        timer = window.after(1000, count_down, minute-1)
    else:
        start_timer()
        marks = ""
        sessions = floor(reps/2)
        for _ in range(sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=80, pady=40, background=BLUE)


# Label, Canvas
title_label = Label(text="Timer", fg=YELLOW, bg=BLUE, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

blank1 = Label(text="blank1", fg=BLUE, bg=BLUE, font=(FONT_NAME, 20))
blank1.grid(column=1, row=1)

canvas = Canvas(width=200, height=224, background=BLUE, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(110, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=2)

blank2 = Label(text="blank2", fg=BLUE, bg=BLUE, font=(FONT_NAME, 20))
blank2.grid(column=1, row=3)


# Button
start_button = Button(text="Start", width=6, height=2, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=4)

reset_button = Button(text="Reset", width=6, height=2, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=4)

check_marks = Label(fg=YELLOW, bg=BLUE)
check_marks.grid(column=1, row=4)

window.mainloop()
