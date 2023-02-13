from turtle import Turtle


class Entity(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()

    def creationEntity(self, arg_listAnswer):
        self.goto(arg_listAnswer[1], arg_listAnswer[2])
        self.write(arg_listAnswer[0])
