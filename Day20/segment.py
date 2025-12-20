import turtle as t

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
