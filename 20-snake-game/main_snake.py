
import time
from segment import *
from score import Score
from food import Food


# game
game_on = True
food = Food()
snake = Snake()
scoreboard = Score()

snake.create_snake()

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.movement()
    snake.control()

    if abs(snake.head.xcor()) > 325 or abs(snake.head.ycor()) > 325:
        scoreboard.game_over()
        game_on = False

    if snake.head.distance(food) < 17:
        food.refresh_food()
        scoreboard.refresh_score()
        snake.add_snake()

    for segment in snake.parts[1:]:
        if snake.head.distance(segment) < 17:
            scoreboard.game_over()
            game_on = False


screen.exitonclick()
