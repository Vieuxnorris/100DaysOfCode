from data import Data
from quiz_brain import QuizBrain
from ui import Ui

quiz = QuizBrain(Data().getQuestions())
quizzUi = Ui(quiz)

