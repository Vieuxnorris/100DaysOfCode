import random
from turtle import Turtle, Screen

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat",
           "SlateGray", "SeaGreen"]


timmy = Turtle()


def DrawingShapes(arg_numberShapes):
    corners = 3
    while corners < arg_numberShapes:
        cornersAngle = 360 / corners
        timmy.color(random.choice(colours))
        for _ in range(corners):
            timmy.forward(100)
            timmy.right(cornersAngle)
        corners += 1


DrawingShapes(10)
screen = Screen()
screen.exitonclick()
