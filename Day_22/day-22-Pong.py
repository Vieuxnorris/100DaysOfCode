from turtle import Screen
from pingpong import PingPong
from score import Score
from ball import Ball
import time

# Global Variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR_MODE = 255
SCREEN_COLOR = "black"

# Variable
endGame = False
moveDown = False

screen = Screen()
screen.title("Pong")
screen.colormode(SCREEN_COLOR_MODE)
screen.bgcolor(SCREEN_COLOR)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

pingPong = PingPong()
score = Score()
ball = Ball()

screen.listen()
screen.onkeypress(pingPong.moveUp, "Up")
screen.onkeypress(pingPong.moveDown, "Down")

while not endGame:
    screen.update()
    time.sleep(ball.speedGame)
    ball.move()

    if not moveDown:
        moveDown = pingPong.AIMoveUp()
    else:
        moveDown = pingPong.AIMoveDown()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    if ball.distance(pingPong.listEntity[1]) < 60 and ball.xcor() > 370 or\
            ball.distance(pingPong.listEntity[0]) < 60 and ball.xcor() < -370:
        ball.bounceX()

    if ball.xcor() > 400 or ball.xcor() < -400:
        score.update(ball.xcor())
        ball.goal()

screen.exitonclick()
