from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
BEIGE = "#FEFBE9"
GREEN = "#183A1D"
SAGE = "#E1EEDD"
ORANGE = "#F0A04B"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
RESP = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #

def resetTimer():
    global RESP, TIMER
    window.after_cancel(TIMER)
    checkBreak.config(text="")
    RESP = 0
    labelTimer.config(text="Timer")
    canvas.itemconfig(timerText, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timerMechanism():
    global RESP
    RESP += 1

    workSec = WORK_MIN * 60
    shortBreakSec = SHORT_BREAK_MIN * 60
    longBreakMin = LONG_BREAK_MIN * 60

    if RESP % 8 == 0:
        countDown(longBreakMin)
        labelTimer.config(text="Long Break", font=(FONT_NAME, 35, "bold"), bg=BEIGE, fg=GREEN)
    elif RESP % 2 == 0:
        countDown(shortBreakSec)
        labelTimer.config(text="Short Break", font=(FONT_NAME, 35, "bold"), bg=BEIGE, fg=SAGE)
    else:
        countDown(workSec)
        labelTimer.config(text="Work!", font=(FONT_NAME, 35, "bold"), bg=BEIGE, fg=ORANGE)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countDown(count):
    minutes = math.floor(count / 60)
    secondes = count % 60
    canvas.itemconfig(timerText, text=f"{minutes}:{secondes:02d}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, countDown, count - 1)
    else:
        timerMechanism()
        marks = ""
        work_session = math.floor(RESP/2)
        for _ in range(work_session):
            marks += "✔"
        checkBreak.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(width=500, height=600)
window.config(bg=BEIGE, pady=150, padx=125)

# Label
labelTimer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=BEIGE, fg=ORANGE)
labelTimer.grid(column=1, row=0)

# Canvas
canvas = Canvas(width=200, height=223, bg=BEIGE, highlightthickness=0)
tomatoImg = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=tomatoImg)
timerText = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Button
buttonStart = Button(width=5, text="Start", highlightthickness=0)
buttonStart.config(command=timerMechanism)
buttonStart.grid(column=0, row=2)
buttonReset = Button(width=5, text="Reset", highlightthickness=0)
buttonReset.config(command=resetTimer)
buttonReset.grid(column=2, row=2)

# Label
checkBreak = Label(font=(FONT_NAME, 15), bg=BEIGE, fg=ORANGE)
checkBreak.grid(column=1, row=3)

window.mainloop()
