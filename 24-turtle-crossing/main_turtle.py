
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE = 280

# screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# player movement
turtle = Player()
screen.listen()
screen.onkey(turtle.move_forward, "Up")

# car movement
cars = CarManager()

# score
level = 1
scores = Scoreboard()
scores.write_score(level)

# game
game_on = True
increment = 0

while game_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.car_move(increment)

    if turtle.ycor() > FINISH_LINE:
        increment += 2
        turtle.back_home()

        level += 1
        scores.write_score(level)

    for car in cars.all_cars:
        if turtle.distance(car) < 20:
            game_on = False

scores.write_game_over()
screen.exitonclick()
