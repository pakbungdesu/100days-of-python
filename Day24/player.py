
from turtle import Turtle

STARTING_POS = (0, -280)
DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.left(90)
        self.setpos(STARTING_POS)

    def move_forward(self):
        self.forward(DISTANCE)

    def back_home(self):
        self.setpos(STARTING_POS)
