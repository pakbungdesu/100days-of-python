
from turtle import Turtle

FONT = ("Courier", 15, "normal")
SCORE_POS = (-280, 280)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(SCORE_POS)

    def write_score(self, level):
        self.clear()
        self.write(f"Level {level}", False, "left", FONT)

    def write_game_over(self):
        self.home()
        self.write("Game over", False, "center", FONT)
