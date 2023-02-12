from turtle import Turtle
import random

# Global variables
COLOR_SNAKE = "white"
SHAPE_SNAKE = "square"
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

# Variables
startingPositions = [(0, 0), (-20, 0), (-40, 0)]


def randomColor(body):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    RGB = (r, g, b)
    body.color(RGB)


class Snake:
    def __init__(self):
        self.bodySnake = []
        for position in startingPositions:
            self.addSegments(position)
        self.head = self.bodySnake[0]

    def createSnake(self):
        for position in startingPositions:
            self.addSegments(position)
        self.head = self.bodySnake[0]

    def addSegments(self, position):
        body = Turtle(shape=SHAPE_SNAKE)
        body.penup()
        randomColor(body)
        body.goto(position)
        self.bodySnake.append(body)

    def extendBody(self):
        self.addSegments(self.bodySnake[-1].position())

    def move(self):
        for indexSnakeBody in range(len(self.bodySnake) - 1, 0, -1):
            new_x = self.bodySnake[indexSnakeBody - 1].xcor()
            new_y = self.bodySnake[indexSnakeBody - 1].ycor()
            self.bodySnake[indexSnakeBody].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for seg in self.bodySnake:
            seg.goto(1000, 1000)
        self.bodySnake.clear()
        self.createSnake()

    def verifBodySnake(self):
        for segment in self.bodySnake[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def verifWall(self):
        if self.bodySnake[0].xcor() > 280 or self.bodySnake[0].xcor() < -280 \
                or self.bodySnake[0].ycor() > 280 or self.bodySnake[0].ycor() < -280:
            return True
        return False
