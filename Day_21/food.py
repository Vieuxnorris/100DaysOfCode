from turtle import Turtle
import random

# Global Variable
FOOD_SHAPE = "circle"
FOOD_COLOR = "green"
FOOD_SIZE = 0.5


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.randomColor()
        self.shapesize(stretch_len=FOOD_SIZE, stretch_wid=FOOD_SIZE)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        tuple_random = (random_x, random_y)
        self.randomColor()
        self.goto(tuple_random)

    def randomColor(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        RGB = (r, g, b)
        self.color(RGB)
