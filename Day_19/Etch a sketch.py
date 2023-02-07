from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def moveForward():
    timmy.forward(10)


def moveBackward():
    timmy.backward(10)


def moveClockwise():
    timmy.setheading(timmy.heading() + 5)


def moveCounterClockwise():
    timmy.setheading(timmy.heading() - 5)


def clearDrawing():
    timmy.reset()


screen.onkeypress(moveForward, 'w')
screen.onkeypress(moveBackward, 's')
screen.onkeypress(moveCounterClockwise, 'a')
screen.onkeypress(moveClockwise, 'd')
screen.onkeypress(clearDrawing, 'c')
screen.listen()
screen.exitonclick()
