
from turtle import Turtle

# constant
ALIGN = "center"
FONT = ("Courier", 70, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")

        self.l_score = 0
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGN, font=FONT)

        self.r_score = 0
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def update_score(self, paddle_win):
        if paddle_win == "left":
            self.clear()
            self.l_score += 1
            self.goto(-100, 200)
            self.write(self.l_score, align=ALIGN, font=FONT)

            self.goto(100, 200)
            self.write(self.r_score, align=ALIGN, font=FONT)
        else:
            self.clear()
            self.r_score += 1
            self.goto(100, 200)
            self.write(self.r_score, align=ALIGN, font=FONT)

            self.goto(-100, 200)
            self.write(self.l_score, align=ALIGN, font=FONT)
