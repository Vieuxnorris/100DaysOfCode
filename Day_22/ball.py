from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5)
        self.penup()
        self.color("red")
        self.x_pos = 10
        self.y_pos = 10
        self.speedGame = 0.1

    def move(self):
        new_x = self.xcor() + self.x_pos
        new_y = self.ycor() + self.y_pos
        self.goto(new_x, new_y)

    def bounceY(self):
        self.y_pos *= -1

    def bounceX(self):
        self.speedGame *= 0.9
        self.x_pos *= -1

    def goal(self):
        self.goto(0, 0)
        self.bounceX()
