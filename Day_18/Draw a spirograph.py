import random
from turtle import Turtle, Screen

directions = [0, 90, 180, 270]


timmy = Turtle()
screen = Screen()
screen.colormode(255)


def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colorRGB = (r, g, b)
    return colorRGB


def drawSpirograph(arg_size):
    timmy.speed(0)
    for _ in range(360 // arg_size):
        timmy.color(randomColor())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + arg_size)


drawSpirograph(5)
screen.exitonclick()
