from art import logo
from replit import clear
import random

# global
RANDOM_NUMBER = random.randint(1,100)

# variables
lives = 0
goodAnswer = False

# logo and early code
clear()
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

print(f"Pssst, the correct answer is {RANDOM_NUMBER}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if "easy" in difficulty:
    lives = 10
else:
    lives = 5

# fonction
def checkAnswer(answer):
    if answer > RANDOM_NUMBER:
        print("Too high.")
        return False
    elif answer < RANDOM_NUMBER:
        print("Too low.")
        return False
    else:
        return True

def game(lives):
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

# Game
goodAnswer = game(lives=lives)

if goodAnswer == True:
    print(f"You got it! The answer was {RANDOM_NUMBER}")
else:
    print("You've run out of guesses, you lose.")
