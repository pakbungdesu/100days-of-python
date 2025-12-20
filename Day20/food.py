from turtle import Turtle
import random as rand

class Food(Turtle):
    """
    A class that represents the food in the Snake Game.
    Inherits from the Turtle class to render food on the screen.
    """
    def __init__(self):
        """
        Initializes the food object, setting its shape, color,
        and initial random position.
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        # Scale the circle down to 10x10 pixels (half the default size)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        """
        Moves the food to a new random location within the screen boundaries.
        """
        rand_x = rand.randint(-280, 280)
        rand_y = rand.randint(-280, 280)
        self.goto(rand_x, rand_y)
