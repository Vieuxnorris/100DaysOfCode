from turtle import Turtle

# Global Variables
SCORE_COLOR = "white"
SCORE_ALIGN = "center"
SCORE_FONT = ("Arial", 20, 'normal')
GAME_OVER_POSITION = (0, 0)


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color(SCORE_COLOR)
        self.penup()
        self.goto(-340, 260)
        self.write(f"Level = {self.level}", align=SCORE_ALIGN, font=SCORE_FONT)
        self.ht()
        self.gameSpeed = 0.1

    def gameOver(self):
        self.goto(GAME_OVER_POSITION)
        self.write(f"GAME OVER", align=SCORE_ALIGN, font=SCORE_FONT)

    def update(self):
        self.level += 1
        self.clear()
        self.write(f"Level = {self.level}", align=SCORE_ALIGN, font=SCORE_FONT)
        self.gameSpeed *= 0.8
