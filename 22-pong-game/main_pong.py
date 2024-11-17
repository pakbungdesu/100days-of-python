
import time
from paddle_class import *
from ball_class import *
from score_class import *

screen.tracer(0)

# create paddle
padL = Pad(370, 0)
padL.create_pad()
padR = Pad(-370, 0)
padR.create_pad()


# create onkey
screen.listen()
screen.onkey(padL.go_up, "Up")
screen.onkey(padL.go_down, "Down")
screen.onkey(padR.go_up, "w")
screen.onkey(padR.go_down, "s")

# create ball
ball = Ball()

# scoreboard
scoreboard = Score()


# loop
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_edge()

    if ball.distance(padL) < 40 and ball.xcor() > -350 or ball.distance(padR) < 40 and ball.xcor() < 350:
        ball.bounce_pad()

    if ball.xcor() > 400:
        scoreboard.update_score("left")
        ball.move_speed = 0.1
        ball.setpos(0, 0)

    if ball.xcor() < -400:
        scoreboard.update_score("right")
        ball.move_speed = 0.1
        ball.setpos(0, 0)

screen.exitonclick()
