from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 250
CANVAS_FONT = ("Arial", 20, "italic")


class Ui:
    def __init__(self, quizBrain: QuizBrain):
        self.quiz = quizBrain

        # ---------------------------- UI SETUP ------------------------------- #

        # Screen
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Label
        self.scoreLabel = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.scoreLabel.grid(column=1, row=0)

        # Canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvasText = self.canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/2,
                                                  text="test", width=CANVAS_WIDTH, font=CANVAS_FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # PhotoImages
        self.rightImage = PhotoImage(file="./images/true.png")
        self.wrongImage = PhotoImage(file="./images/false.png")

        # Button
        self.rightButton = Button(image=self.rightImage, highlightthickness=0,
                                  bg=THEME_COLOR, command=self.rightButtonClick)
        self.rightButton.grid(column=0, row=2)
        self.wrongButton = Button(image=self.wrongImage, highlightthickness=0,
                                  bg=THEME_COLOR, command=self.wrongButtonClick)
        self.wrongButton.grid(column=1, row=2)

        self.getNextQuestion()
        # Mainloop
        self.window.mainloop()

    def rightButtonClick(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrongButtonClick(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def getNextQuestion(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            qText = self.quiz.next_question()
            self.scoreLabel.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.canvasText, text=qText)
        else:
            self.canvas.itemconfig(self.canvasText, text="You've reached the end of the quizzler.")
            self.rightButton.config(state="disabled")
            self.wrongButton.config(state="disabled")

    def give_feedback(self, answer: bool):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.getNextQuestion)
