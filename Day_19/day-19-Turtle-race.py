import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)

listTurtle = []

userBet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
winTurtle = Turtle()


minus = 0
for turtle_index in range(6):
    timmy = Turtle(shape='turtle')
    timmy.color(colors[turtle_index])
    timmy.penup()
    timmy.goto(x=-220, y=(-100 + minus))
    listTurtle.append(timmy)
    minus += 30

win = False
while not win:
    for turtle in listTurtle:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= 230:
            win = True
            winTurtle = turtle

if winTurtle.pencolor() == userBet:
    print(f"You've won! The {winTurtle.pencolor()} turtle is the winner!")
else:
    print(f"You've won! The {winTurtle.pencolor()} turtle is the winner!")

screen.exitonclick()
