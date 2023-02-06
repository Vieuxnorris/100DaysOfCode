class QuizBrain:
    def __init__(self, questionList):
        self.question_number = 0
        self.questionsList = questionList
        self.validQuestions = 0

    def NextQuestion(self):
        current_question = self.questionsList[self.question_number]
        userChoice = input(f"Q.{self.question_number + 1}: {current_question.text}"
                           f" (True/False): ").lower()
        if self.IsValid(userChoice):
            self.validQuestions += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        self.question_number += 1
        print(f"The correct answer was: {current_question.answer}.")
        if not self.StillHasQuestion():
            print("You've completed the quiz")
            print(f"Your final score was: {self.validQuestions}/{self.question_number}")
        else:
            print(f"Your current score is: {self.validQuestions}/{self.question_number}")

    def StillHasQuestion(self):
        return self.question_number < len(self.questionsList)

    def IsValid(self, userChoice):
        return self.questionsList[self.question_number].answer.lower() == userChoice
