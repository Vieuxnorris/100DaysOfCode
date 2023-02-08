from turtle import Screen
from Snake import Snake
import time

# Global Variables
BACKGROUND_COLOR = "black"


# Variables
endGame = False

screen = Screen()
screen.bgcolor(BACKGROUND_COLOR)
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while not endGame:
    screen.update()
    time.sleep(0.1)
    endGame = snake.verifWall()
    snake.move()

screen.exitonclick()
