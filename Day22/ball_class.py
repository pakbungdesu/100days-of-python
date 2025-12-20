from turtle import Turtle

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
