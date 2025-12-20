from turtle import Turtle
import random as rand

# --- Constants ---
START_X = 300
STARTING_POS = (-280, -280)
DISTANCE = 5
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager(Turtle):
    """
    Manages the generation and movement of car objects.
    Acts as a controller for a list of Turtle objects representing traffic.
    """

    def __init__(self):
        """Initializes the manager and an empty list to store car objects."""
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.penup()
        self.setpos(STARTING_POS)

    def create_car(self):
        """
        Randomly creates a new car at the right edge of the screen.
        The chance of creation is 1 in 6 per game loop iteration.
        """
        # Controls the density of traffic
        rand_n = rand.randrange(1, 7)
        if rand_n == 1:
            new_car = Turtle("square")
            new_car.penup()
            # Stretches the square into a rectangle (width=40px, height=20px)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(rand.choice(COLORS))

            # Choose a random vertical lane
            rand_y = rand.randrange(-250, 250)
            new_car.setpos((START_X, rand_y))

            self.all_cars.append(new_car)

    def car_move(self, increment):
        """
        Moves all active cars from right to left.

        Args:
            increment (int): The additional speed added as the player levels up.
        """
        for car in self.all_cars:
            # Cars move 'backward' because they face East (0) by default
            # but need to move West.
            car.backward(DISTANCE + increment)
