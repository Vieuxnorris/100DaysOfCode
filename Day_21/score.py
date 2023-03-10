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
        self.score = 0
        self.color(SCORE_COLOR)
        self.penup()
        self.goto(SCORE_POSITION)
        self.write(f"Score = {self.score}", align=SCORE_ALIGN, font=SCORE_FOND)
        self.ht()

    def gameOver(self):
        self.goto(GAME_OVER_POSITION)
        self.write("GAME OVER", align=SCORE_ALIGN, font=SCORE_FOND)

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align=SCORE_ALIGN, font=SCORE_FOND)
