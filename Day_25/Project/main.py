from turtle import Screen
from csvnormalisation import CsvNormalisation
from entity import Entity

# Global Variables
SCREEN_WIDTH = 729
SCREEN_HEIGHT = 491

screen = Screen()
dataFrame = CsvNormalisation()
entity = Entity()

screen.title("U.S. States game")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgpic("blank_states_img.gif")
screen.tracer(0)

totalCorrectAnswer = 0
maxScore = 50
listInfos = []

endGame = False
while not endGame:
    screen.update()
    userChoice = screen.textinput(title=f"{totalCorrectAnswer}/50 States Correct",
                                  prompt="What's another state name?").lower().title()
    if dataFrame.correctAnswer(userChoice):
        listInfos = dataFrame.returnFullInfos()
        entity.creationEntity(listInfos)
        totalCorrectAnswer += 1
    maxScore -= 1
    print(maxScore)
    if maxScore <= 0:
        endGame = dataFrame.returnEndGame()



screen.exitonclick()
