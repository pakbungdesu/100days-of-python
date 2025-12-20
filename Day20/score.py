from turtle import Turtle

# Constants for consistent text styling across the game
ALIGN = "center"
FONT = ("Courier", 13, "normal")


class Score(Turtle):
    """
    Manages the game scoring system, including rendering the current score
    on screen and persisting the high score to a external file.
    """

    def __init__(self):
        """
        Initializes the scoreboard, loads the historical high score from 'score_record.txt',
        and displays the initial score at the top of the screen.
        """
        super().__init__()
        # --- File I/O: Load High Score ---
        try:
            with open("score_record.txt", mode="r") as f:
                # Reads the last line of the file to get the most recent high score
                highest_score = f.readlines()[-1]
                self.highest = int(highest_score)
        except (FileNotFoundError, IndexError):
            # Fallback if the file doesn't exist or is empty
            self.highest = 0

        # --- UI Setup ---
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)  # Positioned at the top-center
        self.score = 0
        self.update_display()

    def update_display(self):
        """Helper method to rewrite the current and high score to the screen."""
        self.clear()
        self.write(f"Score: {self.score} | Highest score: {self.highest}",
                   False, align=ALIGN, font=FONT)

    def refresh_score(self):
        """Increments the current score and updates the on-screen display."""
        self.score += 1
        self.update_display()

    def game_over(self):
        """
        Triggers the Game Over sequence. Checks if a new high score was achieved
        and saves it to 'score_record.txt' if necessary.
        """
        self.clear()

        # --- Persistent Storage Logic ---
        if self.score > self.highest:
            self.highest = self.score
            with open("score_record.txt", mode="a") as f:
                # Append the new high score to the record file
                f.write(f"\n{self.score}")

        # --- Final Score Display ---
        self.goto(0, 20)
        self.write("Game Over", False, align=ALIGN, font=FONT)
        self.goto(0, 0)
        self.write(f"Total score: {self.score}", False, align=ALIGN, font=FONT)
        self.goto(0, -20)
        self.write(f"Highest score: {self.highest}", False, align=ALIGN, font=FONT)
