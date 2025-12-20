from turtle import Turtle

# --- Constants ---
# ALIGN: Horizontal placement of text relative to the turtle's position
# FONT: A tuple containing (Family, Size, Weight)
ALIGN = "center"
FONT = ("Courier", 70, "normal")


class Score(Turtle):
    """
    Manages and displays the scores for both the left and right players.
    Inherits from Turtle to use the .write() method for rendering text.
    """

    def __init__(self):
        """Initializes the score values and draws the starting scoreboard (0 | 0)."""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")

        # Player scores
        self.l_score = 0
        self.r_score = 0

        # Initial display
        self.refresh_display()

    def refresh_display(self):
        """Clears the previous score and redraws the current scores on both sides."""
        self.clear()

        # Display Left Player Score
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGN, font=FONT)

        # Display Right Player Score
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def update_score(self, paddle_win):
        """
        Increments the score of the winning player and refreshes the screen.

        Args:
            paddle_win (str): Either "left" or "right", indicating which player scored.
        """
        if paddle_win == "left":
            self.l_score += 1
        else:
            self.r_score += 1

        self.refresh_display()
