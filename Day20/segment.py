
import turtle as t

# setting
screen = t.Screen()
screen.title("My Snake Game")
screen.setup(width=650, height=650)
screen.bgcolor("black")
screen.tracer(0)

# constant
START_POS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
DISTANCE = 20

# class
class Snake:
    def __init__(self):
        self.parts = []
        self.game_on = True

        # here is important
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        for pos in START_POS:
            p = t.Turtle(shape="square")
            p.setpos(pos)
            p.speed(1)
            p.color("white")
            p.penup()
            self.parts.append(p)


    def movement(self):
        for p_num in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[p_num - 1].xcor()
            new_y = self.parts[p_num - 1].ycor()
            self.parts[p_num].goto(new_x, new_y)

        self.head.forward(DISTANCE)


    def control(self):
        def head_up():
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
        if self.head.heading() == UP:
            last_x = self.parts[-1].xcor()
            last_y = self.parts[-1].ycor()

            new_y = last_y - 20
            pos = (last_x, new_y)

            p = t.Turtle(shape="square")
            p.setpos(pos)
            p.color("white")
            p.penup()
            self.parts.append(p)

        elif self.head.heading() == DOWN:
            last_x = self.parts[-1].xcor()
            last_y = self.parts[-1].ycor()

            new_y = last_y + 20
            pos = (last_x, new_y)

            p = t.Turtle(shape="square")
            p.setpos(pos)
            p.color("white")
            p.penup()
            self.parts.append(p)

        elif self.head.heading() == RIGHT:
            last_x = self.parts[-1].xcor()
            last_y = self.parts[-1].ycor()

            new_x = last_x - 20
            pos = (new_x, last_y)

            p = t.Turtle(shape="square")
            p.setpos(pos)
            p.color("white")
            p.penup()
            self.parts.append(p)

        else:
            last_x = self.parts[-1].xcor()
            last_y = self.parts[-1].ycor()

            new_x = last_x + 20
            pos = (new_x, last_y)

            p = t.Turtle(shape="square")
            p.setpos(pos)
            p.color("white")
            p.penup()
            self.parts.append(p)
