import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=750, height= 650)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
correct_answers = []

while len(correct_answers) < 50:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_answers = [state for state in states if state not in correct_answers]
        df = pandas.DataFrame(missing_answers)
        df.to_csv("missing_states")
        break
    if answer_state in states and answer_state not in correct_answers:
        correct_answers.append(answer_state)
        answer = turtle.Turtle()
        x_and_y = data[data.state == answer_state]
        x_cor = x_and_y.x
        y_cor = x_and_y.y
        answer.penup()
        answer.hideturtle()
        answer.goto(int(x_cor), int(y_cor))
        answer.write(answer_state, align="center")
