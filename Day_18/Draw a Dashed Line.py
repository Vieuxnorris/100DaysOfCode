from turtle import Turtle, Screen

timmy = Turtle()


def DashedLine(arg_forward, arg_espace):
    timmy.forward(arg_forward)
    timmy.penup()
    timmy.forward(arg_espace)
    timmy.pendown()


for _ in range(10):
    DashedLine(10, 20)

screen = Screen()
screen.exitonclick()
