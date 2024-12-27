
from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 13, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        # read the highest score in history
        with open("score_record.txt", mode="r") as f:
            highest_score = f.readlines()[-1]
            highest_score = int(highest_score)

        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 300)
        self.score = 0
        self.highest = highest_score
        self.write(f"Score: {self.score} | Highest score: {self.highest}", False, align=ALIGN, font=FONT)


    def refresh_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} | Highest score: {self.highest}", False, align=ALIGN, font=FONT)


    def game_over(self):
        self.clear()
        if self.score > self.highest:
            self.highest = self.score
            with open("score_record.txt", mode="a") as f:
                f.write(f"\n{self.score}")

        self.goto(0, 20)
        self.write("Game Over", False, align=ALIGN,font=FONT)
        self.goto(0, 0)
        self.write(f"Total score: {self.score}", False, align=ALIGN, font=FONT)
        self.goto(0, -20)
        self.write(f"Highest score: {self.highest}", False, align=ALIGN, font=FONT)
