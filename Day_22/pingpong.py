from turtle import Turtle

# Global Variables
ENTITY_SIZE_WID = 5
ENTITY_SIZE_LEN = 0.5
ENTITY_COLOR = "white"
ENTITY_SHAPE = "square"

# Variable
positionPingPong = [(-390, 0), (380, 0)]


class PingPong:
    def __init__(self):
        self.listEntity = []
        self.createPingPong()

    def createPingPong(self):
        for position in positionPingPong:
            entity = Turtle(ENTITY_SHAPE)
            entity.penup()
            entity.goto(position)
            entity.color(ENTITY_COLOR)
            entity.shapesize(stretch_wid=ENTITY_SIZE_WID, stretch_len=ENTITY_SIZE_LEN)
            self.listEntity.append(entity)

    def moveUp(self):
        if self.listEntity[0].ycor() > 255:
            pass
        else:
            self.listEntity[0].sety(self.listEntity[0].ycor() + 20)

    def moveDown(self):
        if self.listEntity[0].ycor() < -255:
            pass
        else:
            self.listEntity[0].sety(self.listEntity[0].ycor() - 20)

    def AIMoveUp(self):
        if self.listEntity[1].ycor() < 260:
            self.listEntity[1].sety(self.listEntity[1].ycor() + 10)
            return False
        return True

    def AIMoveDown(self):
        if self.listEntity[1].ycor() > -260:
            self.listEntity[1].sety(self.listEntity[1].ycor() - 10)
            return True
        return False
