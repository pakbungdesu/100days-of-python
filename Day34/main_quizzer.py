"""
Quizzler App - Main Controller
This script integrates the QuizBrain logic with the Tkinter UI.
It handles user interactions, evaluates answers, and manages the visual feedback loop.
"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# ------------------ CONSTANTS ---------------------- #
# UI Styling constants for consistency across the application
THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
BLACK = "#000000"
GREEN = "#E1FFBB"
RED = "#FFC5C5"
FALSE_IMG = "images/false.png"
TRUE_IMG = "images/true.png"
FONT = ("Arial", 15, "italic")
FONT_NAME = "Arial"

# ------------------ EVENT HANDLING ---------------------- #

def handle_true():
    """Callback function for the 'True' button."""
    check_answer("True")

def handle_false():
    """Callback function for the 'False' button."""
    check_answer("False")

def check_answer(user_answer):
    """
    Core game logic: Checks the answer, updates the UI score,
    provides color feedback, and schedules the next question.
    """
    # results[0] is correct/incorrect status, results[1] is the formatted score string
    results = quiz.check_answer(user_answer)
    ui.write_score_label(THEME_COLOR, WHITE, results[1], FONT_NAME, 10)

    # Visual Feedback: Change canvas color based on correctness
    if results[0] == 1:
        ui.set_canvas(300, 250, GREEN)
        ui.write_canvas(150, 125, 280, "Right!", BLACK, FONT)
    else:
        ui.set_canvas(300, 250, RED)
        ui.write_canvas(150, 125, 280, "Wrong!", BLACK, FONT)

    # Progression Logic
    if quiz.still_has_questions():
        # .after() allows for a 1-second pause so the user sees the color feedback
        ui.window.after(1000, lambda: ui.set_canvas(300, 250, WHITE))
        ui.window.after(1000, next_question)
    else:
        ui.window.after(1000, show_final_message)

def show_final_message():
    """Displays the final score and disables interaction at the end of the quiz."""
    final_txt = f"Quiz Complete!\nFinal score: {quiz.score}/{quiz.question_number}"
    ui.set_canvas(300, 250, WHITE)
    ui.write_canvas(150, 125, 280, final_txt, BLACK, FONT)

    # Prevent further clicks after game ends
    ui.right.config(state="disabled")
    ui.wrong.config(state="disabled")

def next_question():
    """Fetches the next question from QuizBrain and renders it to the UI."""
    text = quiz.next_question()
    ui.write_canvas(150, 125, 280, text, BLACK, FONT)

# ------------------ UI INITIALIZATION -------------------- #
ui = QuizInterface()
ui.set_window("Quizzler", 20, 20, THEME_COLOR)
ui.set_canvas(300, 250, WHITE)
ui.set_blank(" ", THEME_COLOR, THEME_COLOR, FONT_NAME)
ui.set_button(TRUE_IMG, FALSE_IMG, handle_true, handle_false)
ui.write_score_label(THEME_COLOR, WHITE, "0/0", FONT_NAME, 10)

# ------------------ DATA PROCESSING -------------------- #
# Converting raw dictionary data from data.py into a list of Question objects
question_bank = []
for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

# Initialize the logic engine with the question bank
quiz = QuizBrain(question_bank)

# Display the first question to start the game
next_question()

# Start the Tkinter event loop
ui.run()
