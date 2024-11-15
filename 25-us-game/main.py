
import turtle as t
import pandas as pd

# screen
screen = t.Screen()
screen.title("U.S. States Game")
screen.setup(800, 500)
image = "states_img.gif"
screen.bgpic(image)
screen.tracer(0)

# turtle
t.hideturtle()

# write states name
df = pd.read_csv("50_states.csv")
states = df["state"].to_list()

# answer
unique = []

while True:
    answer = screen.textinput(f"{len(unique)}/50 States Correct", "What's another state's name")
    answer = answer.title()

    if answer == "Exit":
        learn_more = [ele for ele in states if ele not in unique]
        learn_more = pd.DataFrame(learn_more)
        learn_more.to_csv("missing_states.csv")
        break

    if answer in states and answer not in unique:
        unique.append(answer)
        correct = df[df.state == answer]
        t.penup()
        t.setpos(correct.x.item(), correct.y.item())
        t.pendown()
        t.write(answer, False, "center", ('Arial', 8, 'normal'))

    if len(unique) == 50:
        print("Complete!")
        break

screen.exitonclick()
