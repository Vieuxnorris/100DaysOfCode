# Import
from tkinter import *
import pandas as pd
import random

# Global Variables
CARD_FRONT_WIDTH = 800
CARD_FRONT_HEIGHT = 526
FONT_WORD = ("Ariel", 60, "bold")
FONT_TITLE = ("Ariel", 40, "italic")
WINDOW_COLOR_BG = "#B1DDC6"
COUNT = 3
TIMER = None
DATA_FRAME = None
WORD_DICO = {}

try:
    DATA_FRAME = pd.read_csv("./Dico/wordsToLean.csv")
except FileNotFoundError:
    print("CSV not found")
    DATA_FRAME = pd.read_csv("./Dico/Frequency.csv")
finally:
    toLearn = DATA_FRAME.to_dict(orient="records")


# ---------------------------- RIGHT BUTTON ------------------------------- #

def correctAnswer():
    toLearn.remove(WORD_DICO)
    print(len(toLearn))
    data = pd.DataFrame(toLearn)
    data.to_csv("./Dico/wordsToLean.csv", index=False)
    timerSwitch()


# ---------------------------- TIMER ------------------------------- #
def timerSwitch():
    global TIMER, DATA_FRAME, WORD_DICO
    if len(DATA_FRAME) == 0:
        DATA_FRAME = pd.read_csv("./Dico/Frequency.csv")
    if TIMER is not None:
        window.after_cancel(TIMER)
    WORD_DICO = random.choice(toLearn)
    canvas.itemconfig(titleCanvas, text="English")
    canvas.itemconfig(wordCanvas, text=WORD_DICO['English'])
    canvas.itemconfig(imageCanvas, image=cardFrontImage)
    englishWord(COUNT, WORD_DICO)


# ---------------------------- ENGLISH WORD ------------------------------- #
def englishWord(count, translateList):
    global TIMER
    if count > 0:
        TIMER = window.after(1000, englishWord, count - 1, translateList)
    else:
        canvas.itemconfig(imageCanvas, image=cardBackImage)
        canvas.itemconfig(titleCanvas, text="French")
        canvas.itemconfig(wordCanvas, text=translateList["French"])
        if TIMER is not None:
            window.after_cancel(TIMER)


# ---------------------------- UI SETUP ------------------------------- #

# Screen
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=WINDOW_COLOR_BG)

# Images
cardFrontImage = PhotoImage(file="./Img/card_front.png")
cardBackImage = PhotoImage(file="./Img/card_back.png")
rightButtonImage = PhotoImage(file="./Img/right.png")
wrongButtonImage = PhotoImage(file="./Img/wrong.png")

# Canvas
canvas = Canvas(width=CARD_FRONT_WIDTH, height=CARD_FRONT_HEIGHT, highlightthickness=0, bg=WINDOW_COLOR_BG)
imageCanvas = canvas.create_image(CARD_FRONT_WIDTH / 2, CARD_FRONT_HEIGHT / 2, image=cardFrontImage)
wordCanvas = canvas.create_text(400, 263, text="Word", font=FONT_WORD)
titleCanvas = canvas.create_text(400, 150, text="English", font=FONT_TITLE)
canvas.grid(column=1, row=0, columnspan=2)

# Button
wrongButton = Button(image=wrongButtonImage, highlightthickness=0, bg=WINDOW_COLOR_BG, command=timerSwitch)
wrongButton.grid(column=0, row=1, columnspan=2)
rightButton = Button(image=rightButtonImage, highlightthickness=0, bg=WINDOW_COLOR_BG, command=correctAnswer)
rightButton.grid(column=2, row=1, columnspan=2)

timerSwitch()

window.mainloop()
