import colorgram as colorG
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.ht()
screen = Screen()
screen.colormode(255)


colorsList = []


def extractColorImage():
    colors = colorG.extract("img/dot.jpg", 20)
    for color in colors:
        rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
        colorsList.append(rgb)


def drawDot():
    timmy.setheading(225)
    timmy.forward(300)
    timmy.setheading(0)
    for _ in range(10):
        savePosition = timmy.position()
        for _ in range(10):
            timmy.penup()
            timmy.dot(20, random.choice(colorsList))
            timmy.forward(50)
        timmy.setx(savePosition[0])
        timmy.sety(savePosition[1] + 50)


timmy.penup()
extractColorImage()
drawDot()


screen.exitonclick()
