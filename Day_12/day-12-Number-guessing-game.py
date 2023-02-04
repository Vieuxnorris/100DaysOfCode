from art import logo
from replit import clear
import random

# global
RANDOM_NUMBER = random.randint(1,100)
EASY_MODE = 10
HARD_MODE = 5

# variables
lives = 0
goodAnswer = False

# fonctions
def checkAnswer(answer):
    if answer > RANDOM_NUMBER:
        print("Too high.")
        return False
    elif answer < RANDOM_NUMBER:
        print("Too low.")
        return False
    else:
        return True

def checkLive(lives):
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        answerUser = int(input("Make a guess: "))
        answerProg = checkAnswer(answerUser)
        if answerProg == False:
            lives -= 1
            if lives > 0:
                print("Guess again.")
        else:
            return True
    return False

def game():
    clear()
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    print(f"Pssst, the correct answer is {RANDOM_NUMBER}")

    lives = setDifficulty()
    goodAnswer = checkLive(lives=lives)

    if goodAnswer == True:
        print(f"You got it! The answer was {RANDOM_NUMBER}")
    else:
        print("You've run out of guesses, you lose.")

def setDifficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if "easy" in difficulty:
        return EASY_MODE
    else:
        return HARD_MODE

# Game
game()
