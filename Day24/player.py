from turtle import Turtle

# --- Constants ---
STARTING_POS = (0, -280)
DISTANCE = 10

class Player(Turtle):
    """
    Represents the player-controlled turtle character.
    Handles the movement and position resetting of the turtle.
    """
    def __init__(self):
        """
        Initializes the player as a turtle, sets its orientation
        facing North, and places it at the starting position.
        """
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        # Turn the turtle to face North (Up)
        self.left(90)
        self.setpos(STARTING_POS)

    def move_forward(self):
        """Moves the turtle forward (Up) by the defined distance."""
        self.forward(DISTANCE)

    def back_home(self):
        """Resets the turtle to its starting position at the bottom of the screen."""
        self.setpos(STARTING_POS)
