
import turtle as t
import random as rand

# ------------- FOOD -------------

class Food(t.Turtle):
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


# ------------- SCORE -------------

# Constants for consistent text styling across the game
ALIGN = "center"
FONT = ("Courier", 13, "normal")

class Score(t.Turtle):
    """
    Manages the game scoring system, including rendering the current score
    on screen and persisting the high score to an external file.
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
                content = f.read().strip().split()
                if content:
                    self.highest = int(content[-1])
                else:
                    self.highest = 0
        except FileNotFoundError:
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


# ------------- SEGMENT -------------
# --- Screen & Game Settings ---
screen = t.Screen()
screen.title("My Snake Game")
screen.setup(width=650, height=650)
screen.bgcolor("black")
screen.tracer(0)

# --- Constants ---
START_POS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
DISTANCE = 20

class Snake:
    """
    Manages the snake's body segments, movement logic, and keyboard controls.
    """
    def __init__(self):
        """Initializes the snake with three segments and sets the head."""
        self.parts = []
        self.game_on = True
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        """Creates the initial 3-segment body of the snake at the start positions."""
        for pos in START_POS:
            self._add_segment(pos)

    def _add_segment(self, position):
        """Helper method to create and style a new turtle segment."""
        p = t.Turtle(shape="square")
        p.color("white")
        p.penup()
        p.setpos(position)
        self.parts.append(p)

    def movement(self):
        """
        Moves the snake forward. Each segment moves to the position of the
        segment that was previously in front of it.
        """
        # Range(start, stop, step) - moves segments from tail to head
        for p_num in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[p_num - 1].xcor()
            new_y = self.parts[p_num - 1].ycor()
            self.parts[p_num].goto(new_x, new_y)

        self.head.forward(DISTANCE)

    def control(self):
        """Sets up key listeners and defines movement restrictions."""
        def head_up():
            # Prevent snake from moving directly down if it is moving up
            if self.head.heading() != DOWN:
                self.head.setheading(UP)

        def head_down():
            if self.head.heading() != UP:
                self.head.setheading(DOWN)

        def turn_left():
            if self.head.heading() != RIGHT:
                self.head.setheading(LEFT)

        def turn_right():
            if self.head.heading() != LEFT:
                self.head.setheading(RIGHT)

        screen.listen()
        screen.onkey(head_up, "Up")
        screen.onkey(head_down, "Down")
        screen.onkey(turn_right, "Right")
        screen.onkey(turn_left, "Left")

    def add_snake(self):
        """
        Extends the snake by adding a new segment at the end of the tail
        based on the current direction of movement.
        """
        last_x = self.parts[-1].xcor()
        last_y = self.parts[-1].ycor()

        # Determine where to place the new segment based on heading
        if self.head.heading() == UP:
            pos = (last_x, last_y - 20)
        elif self.head.heading() == DOWN:
            pos = (last_x, last_y + 20)
        elif self.head.heading() == RIGHT:
            pos = (last_x - 20, last_y)
        else: # LEFT
            pos = (last_x + 20, last_y)

        self._add_segment(pos)

def process():
    import time

    screen_local = t.Screen()
    screen_local.setup(width=600, height=600)
    screen_local.bgcolor("black")
    screen_local.tracer(0)

    food = Food()
    snake = Snake()      # Initial 3 segments
    scoreboard = Score()
    snake.control()

    game_on = True
    while game_on:
        screen_local.update()
        time.sleep(0.1)
        snake.movement()

        # Wall Collision
        if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
            scoreboard.game_over()
            game_on = False

        # Food Collision
        if snake.head.distance(food) < 17:
            food.refresh_food()
            scoreboard.refresh_score()
            snake.add_snake()

        # Tail Collision
        for segment in snake.parts[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                game_on = False

    screen_local.exitonclick()


if __name__ == "__main__":
    process()
