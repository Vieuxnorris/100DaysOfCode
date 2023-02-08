from turtle import Turtle

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


class Snake:
    def __init__(self):
        self.bodySnake = []
        for position in startingPositions:
            self.body = Turtle(shape=SHAPE_SNAKE)
            self.body.penup()
            self.color = self.body.color(COLOR_SNAKE)
            self.body.goto(position)
            self.bodySnake.append(self.body)
        self.head = self.bodySnake[0]

    def move(self):
        for indexSnakeBody in range(len(self.bodySnake) - 1, 0, -1):
            new_x = self.bodySnake[indexSnakeBody - 1].xcor()
            new_y = self.bodySnake[indexSnakeBody - 1].ycor()
            self.bodySnake[indexSnakeBody].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == RIGHT:
            self.head.setheading(UP)
        elif self.head.heading() == LEFT:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() == RIGHT:
            self.head.setheading(DOWN)
        elif self.head.heading() == LEFT:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() == UP:
            self.head.setheading(RIGHT)
        elif self.head.heading() == DOWN:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() == UP:
            self.head.setheading(LEFT)
        elif self.head.heading() == DOWN:
            self.head.setheading(LEFT)

    def verifBodySnake(self):
        for segment in self.bodySnake:
            if segment.pos() == self.bodySnake[0].pos():
                return True
        return False

    def verifWall(self):
        if self.bodySnake[0].xcor() >= 280 or self.bodySnake[0].xcor() <= -280\
                or self.bodySnake[0].ycor() >= 280 or self.bodySnake[0].ycor() <= -280:
            return True
        return False
