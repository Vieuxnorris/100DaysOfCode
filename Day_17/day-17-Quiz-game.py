from question_model import QuestionModel
from quiz_brain import QuizBrain
from data import question_data

questionBank = []

for data in question_data:
    questionText = data['question']
    questionAnswer = data['correct_answer']
    newQuestion = QuestionModel(q_text=questionText, q_answer=questionAnswer)
    questionBank.append(newQuestion)

brain = QuizBrain(questionBank)

while brain.StillHasQuestion():
    brain.NextQuestion()
