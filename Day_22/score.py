from turtle import Turtle

# Global Variable
SCORE_COLOR = "white"
SCORE_ALIGN = "center"
SCORE_FOND = ("Arial", 20, 'normal')
SCORE_POSITION = (0, 270)
GAME_OVER_POSITION = (0, 0)


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.color(SCORE_COLOR)
        self.penup()
        self.goto(-100, 265)
        self.write(f"{self.score_l}", align=SCORE_ALIGN, font=SCORE_FOND)
        self.ht()
        self.goto(100, 265)
        self.write(f"{self.score_r}", align=SCORE_ALIGN, font=SCORE_FOND)

    def update(self, positionBall):
        if positionBall < 0:
            self.score_r += 1
        else:
            self.score_l += 1
        self.clear()
        self.goto(-100, 265)
        self.write(f"{self.score_l}", align=SCORE_ALIGN, font=SCORE_FOND)
        self.goto(100, 265)
        self.write(f"{self.score_r}", align=SCORE_ALIGN, font=SCORE_FOND)
