import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state
# print(states)

Game_is_on = True
correct_ans = 0
Guessed_states = []

while len(Guessed_states) < 50:
    user_ans = screen.textinput(title=f"{correct_ans}/50 correct", prompt="What's the next state?").title()
    df = pandas.DataFrame(data)
    if user_ans == "Exit":
        break
    elif user_ans in states.unique():
        Guessed_states.append(user_ans)
        correct_ans += 1
        state_data = data[data.state == user_ans]
        display = turtle.Turtle()
        display.penup()
        display.hideturtle()
        display.goto(int(state_data.x), int(state_data.y))
        display.write(f"{user_ans}", False, "center", font=('Arial', 12, 'bold'))

whole_list = states.to_list()
for i in Guessed_states:
    whole_list.remove(i)

df = pandas.DataFrame(whole_list)
df.to_csv("unanswered_states.csv")

# al = data[data.state == user_ans]


screen.exitonclick()
