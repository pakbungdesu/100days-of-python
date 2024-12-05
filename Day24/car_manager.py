
from turtle import Turtle
import random as rand

START_X = 300
STARTING_POS = (-280, -280)
DISTANCE = 5
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.penup()
        self.setpos(STARTING_POS)

    def create_car(self):
        rand_n = rand.randrange(1, 7)
        if rand_n == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1, 2, 0)
            new_car.color(rand.choice(COLORS))

            rand_y = rand.randrange(-250, 250)
            new_car.setpos((START_X, rand_y))

            self.all_cars.append(new_car)

    def car_move(self, increment):
        for car in self.all_cars:
            car.backward(DISTANCE + increment)
