from turtle import Screen
from player import Player
from entity import Entity
from score import Score
import time


# Global Variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = "black"
SCREEN_MODE = 255

# Variables
dictDifficulty = {"easy": 0.2, "Medium": 0.1, "hard": 0.05}

screen = Screen()
screen.title("Turtle crossing")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)
screen.colormode(SCREEN_MODE)
screen.tracer(0)

player = Player()
entity = Entity()
score = Score()

for _ in range(5):
    entity.createEntity()

endGame = False

userMode = screen.textinput("Choice Difficulty", f"Choice difficulty Easy/Medium/Hard: ").lower()
if userMode in dictDifficulty:
    score.gameSpeed = dictDifficulty[userMode]

screen.listen()
screen.onkeypress(player.move, "Up")

while not endGame:
    time.sleep(score.gameSpeed)
    screen.update()
    entity.move()

    for ent in entity.listEntity:
        if ent.distance(player) < 30:
            endGame = True

    if player.ycor() >= 200:
        score.update()
        player.win()
        entity.update()

score.gameOver()

screen.exitonclick()
