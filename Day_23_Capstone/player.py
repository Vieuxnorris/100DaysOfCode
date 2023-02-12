from turtle import Turtle

# Global Variables
PLAYER_SHAPE = "turtle"
PLAYER_COLOR = "white"


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(PLAYER_SHAPE)
        self.penup()
        self.color(PLAYER_COLOR)
        self.setheading(90)
        self.sety(-200)

    def move(self):
        self.forward(50)

    def win(self):
        self.goto(0, -200)
