
from turtle import Turtle, Screen

# screen setting
screen = Screen()
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.bgcolor("black")


class Pad(Turtle):
    def __init__(self, x_axis, y_axis):
        super().__init__()
        self.x_axis = x_axis
        self.y_axis = y_axis

    def create_pad(self):
        self.penup()
        self.goto(self.x_axis, self.y_axis)
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1, 1)

    def go_up(self):
        current_y = self.ycor()
        current_y += 25
        self.goto(self.x_axis, current_y)

    def go_down(self):
        current_y = self.ycor()
        current_y -= 25
        self.goto(self.x_axis, current_y)
