from turtle import Turtle

# --- Constants ---
# FONT: Defines the typeface, size, and weight for the scoreboard text
FONT = ("Courier", 15, "normal")
# SCORE_POS: The top-left corner of the screen where the level is displayed
SCORE_POS = (-280, 260)


class Scoreboard(Turtle):
    """
    Handles the display of the current level and the game over message.
    Inherits from Turtle to utilize text writing capabilities.
    """

    def __init__(self):
        """
        Initializes the scoreboard turtle, hides the icon,
        and positions it at the top-left of the screen.
        """
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(SCORE_POS)

    def write_score(self, level):
        """
        Clears the previous level text and writes the current level.

        Args:
            level (int): The current level reached by the player.
        """
        self.clear()
        self.write(f"Level: {level}", move=False, align="left", font=FONT)

    def write_game_over(self):
        """
        Moves the turtle to the center of the screen and displays
        the final 'Game over' message.
        """
        self.home()  # Moves to (0,0)
        self.write("GAME OVER", move=False, align="center", font=FONT)
