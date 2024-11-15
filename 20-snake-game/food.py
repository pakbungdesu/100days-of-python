
from turtle import Turtle
import random as rand

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize()
        self.color("blue")
        self.penup()
        self.refresh_food()

    def refresh_food(self):
        rand_x = rand.randint(-300, 300)
        rand_y = rand.randint(-300, 300)
        self.goto(rand_x, rand_y)
