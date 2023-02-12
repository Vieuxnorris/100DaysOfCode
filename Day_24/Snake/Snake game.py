from turtle import Screen
from snake import Snake
from food import Food
from score import Score
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
screen.colormode(255)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while not endGame:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.verifWall() or snake.verifBodySnake():
        snake.reset()
        score.resetScore()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.update()
        snake.extendBody()

screen.exitonclick()
