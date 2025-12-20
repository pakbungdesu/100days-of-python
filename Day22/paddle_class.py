from turtle import Turtle, Screen

# --- Environment Setup ---
# It is usually best to keep screen setup in your main.py,
# but if kept here, it's good to document it as the game window.
screen = Screen()
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.bgcolor("black")


class Pad(Turtle):
    """
    A class to represent a paddle in the Pong game.
    Inherits from Turtle to create a movable rectangle on the screen.
    """

    def __init__(self, x_axis, y_axis):
        """
        Initializes the paddle's starting coordinates.

        Args:
            x_axis (int): The horizontal starting position.
            y_axis (int): The vertical starting position.
        """
        super().__init__()
        self.x_axis = x_axis
        self.y_axis = y_axis

    def create_pad(self):
        """
        Configures the turtle's visual appearance and moves it
        to its assigned starting position.
        """
        self.penup()
        self.goto(self.x_axis, self.y_axis)
        self.shape("square")
        self.color("white")
        # Default square is 20x20. (5, 1) stretches it to 100x20.
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        """Moves the paddle upwards by 25 pixels."""
        current_y = self.ycor()
        current_y += 25
        self.goto(self.x_axis, current_y)

    def go_down(self):
        """Moves the paddle downwards by 25 pixels."""
        current_y = self.ycor()
        current_y -= 25
        self.goto(self.x_axis, current_y)
