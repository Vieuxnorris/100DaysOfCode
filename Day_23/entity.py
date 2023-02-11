from turtle import Turtle
import random

# Global Variables
ENTITY_SHAPE = "square"
ENTITY_RANDOM_MIN = 0
ENTITY_RANDOM_MAX = 255
ENTITY_POSITION_Y = [-150, -100, -50, 0, 50, 100, 150]


def randomColor():
    r = random.randint(ENTITY_RANDOM_MIN, ENTITY_RANDOM_MAX)
    g = random.randint(ENTITY_RANDOM_MIN, ENTITY_RANDOM_MAX)
    b = random.randint(ENTITY_RANDOM_MIN, ENTITY_RANDOM_MAX)
    RGB = (r, g, b)
    return RGB


class Entity:

    def __init__(self):
        self.listEntity = []
        self.speed = random.randint(10, 40)
        self.entity = None

    def createEntity(self):
        body = Turtle(shape=ENTITY_SHAPE)
        body.penup()
        body.color(randomColor())
        body.goto(random.randint(-280, 280), random.choice(ENTITY_POSITION_Y))
        body.shapesize(stretch_len=2)
        self.listEntity.append(body)

    def move(self):
        for entity in self.listEntity:
            self.entity = entity
            new_x = self.entity.xcor() - self.speed
            self.entity.setx(new_x)
            if self.entity.xcor() < -400:
                self.bouncyX()

    def bouncyX(self):
        self.entity.goto(400, random.choice(ENTITY_POSITION_Y))

    def update(self):
        for entity in self.listEntity:
            entity.goto(random.randint(-280, 280), random.choice(ENTITY_POSITION_Y))
