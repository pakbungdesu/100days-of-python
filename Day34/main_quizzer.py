from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# ------------------ CONSTANT ---------------------- #

THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
BLACK = "#000000"
GREEN = "#E1FFBB"
RED = "#FFC5C5"
FALSE = "images/false.png"
TRUE = "images/true.png"
FONT = ("Arial", 15, "italic")
FONT_NAME = "Arial"

# ------------------ UI PART ---------------------- #
def handle_true():
    """Handle the True button click."""
    user_answer = "True"
    check_answer(user_answer)


def handle_false():
    """Handle the False button click."""
    user_answer = "False"
    check_answer(user_answer)


def check_answer(user_answer):
    """Check if the user's answer is correct."""
    results = quiz.check_answer(user_answer)
    ui.write_score_label(THEME_COLOR, WHITE, results[1], FONT_NAME, 10)

    if results[0] == 1:
        ui.set_canvas(300, 250, GREEN)
        ui.write_canvas(150, 125, 280, "Right!", BLACK, FONT)
    else:
        ui.set_canvas(300, 250, RED)
        ui.write_canvas(150, 125, 280, "Wrong!", BLACK, FONT)

    if quiz.still_has_questions():
        ui.window.after(1000, lambda: ui.set_canvas(300, 250, WHITE))  # Reset canvas for next question
        ui.window.after(1000, next_question)  # Wait 1 second, then load the next question
    else:
        ui.window.after(1000, show_final_message)  # Wait 1 second, then show final message


def show_final_message():
    """Show the final completion message."""
    final_txt = f"Quiz Complete! Your final score was: {quiz.score}/{quiz.question_number}"
    ui.set_canvas(300, 250, WHITE)  # Reset the canvas one last time
    ui.write_canvas(150, 125, 280, final_txt, BLACK, FONT)

    # Disable buttons instead of destroying them
    ui.right.config(state="disabled")
    ui.wrong.config(state="disabled")


def next_question():
    """Load the next question onto the UI canvas."""
    text = quiz.next_question()
    ui.write_canvas(150, 125, 280, text, BLACK, FONT)


# ------------------ UI SETUP -------------------- #
ui = QuizInterface()
ui.set_window("My Quizzer", 20, 20, THEME_COLOR)
ui.set_canvas(300, 250, WHITE)
ui.set_blank("A blank", THEME_COLOR, THEME_COLOR, FONT_NAME)
ui.set_button(TRUE, FALSE, handle_true, handle_false)
ui.write_score_label(THEME_COLOR, WHITE, "0/0", FONT_NAME, 10)

# ------------------ QUIZ PART -------------------- #
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
next_question()  # Show the first question

ui.run()
