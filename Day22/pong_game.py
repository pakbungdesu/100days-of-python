from turtle import Turtle, Screen
import time

class Ball(Turtle):
    """
    A class to represent the ball in the Pong game.
    Handles movement logic, wall bouncing, and paddle collisions.
    """
    def __init__(self):
        """Initializes the ball's appearance, position, and movement vectors."""
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        # move_x and move_y determine the direction and "step" size of movement
        self.move_x = 10
        self.move_y = 10
        # move_speed controls the time.sleep() delay in the main loop
        self.move_speed = 0.1

    def move(self):
        """Calculates and moves the ball to its next coordinate position."""
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_edge(self):
        """Inverts the Y-axis direction when the ball hits the top or bottom wall."""
        self.move_y *= -1

    def bounce_pad(self):
        """
        Inverts the X-axis direction when the ball hits a paddle.
        Also increases the ball's speed by reducing the sleep delay.
        """
        self.move_x *= -1
        self.move_speed *= 0.9


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


def process():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.title("My Pong Game")
    screen.bgcolor("black")

    # --- Screen Setup ---
    # tracer(0) stops automatic animation so we can update it manually with screen.update()
    screen.tracer(0)

    # --- Object Initialization ---
    # Create Left and Right paddles at specific screen coordinates
    padR = Pad(370, 0)
    padR.create_pad()
    padL = Pad(-370, 0)
    padL.create_pad()

    # --- Controls ---
    screen.listen()
    # Player 1 (Right side of screen, using Arrow keys)
    screen.onkey(padR.go_up, "Up")
    screen.onkey(padR.go_down, "Down")
    # Player 2 (Left side of screen, using WASD)
    screen.onkey(padL.go_up, "w")
    screen.onkey(padL.go_down, "s")

    # Create the ball and the scoreboard
    ball = Ball()
    scoreboard = Score()

    # --- Main Game Loop ---
    game_on = True
    while game_on:
        # Controls the speed of the game based on the ball's current move_speed
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # --- Wall Collision Logic ---
        # Detect if ball hits the top or bottom wall (approx 300 height)
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_edge()

        # --- Paddle Collision Logic ---
        # distance() < 40: checks if the ball is close to the center of the paddle
        # xcor() checks: ensure the ball is actually at the horizontal position of the paddle
        if ball.distance(padR) < 40 and ball.xcor() > 340 or ball.distance(padL) < 40 and ball.xcor() < -340:
            ball.bounce_pad()

        # --- Score & Goal Logic ---
        # Ball goes past Left paddle (Right player scores)
        if ball.xcor() > 400:
            scoreboard.update_score("right")
            ball.move_speed = 0.1  # Reset speed for next round
            ball.setpos(0, 0)  # Reset ball position
            ball.bounce_pad()  # Launch ball towards the other player

        # Ball goes past Right paddle (Left player scores)
        if ball.xcor() < -400:
            scoreboard.update_score("left")
            ball.move_speed = 0.1
            ball.setpos(0, 0)
            ball.bounce_pad()

    screen.exitonclick()


if __name__ == "__main__":
    process()