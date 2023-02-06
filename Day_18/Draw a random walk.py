import random
from turtle import Turtle, Screen

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat",
           "SlateGray", "SeaGreen"]
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

def drawRandomWalk():
    timmy.pensize(3)
    timmy.speed(0)
    for _ in range(300):
        timmy.color(randomColor())
        timmy.setheading(random.choice(directions))
        timmy.forward(20)


drawRandomWalk()
screen.exitonclick()
