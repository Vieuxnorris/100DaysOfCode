from replit import clear
from art import logo, vs
from game_data import data
import random

# Global
SCORE = 0

# Functions
def game():
    endGame = False
    while endGame != True:
        clear()
        print(logo)
        endGame = displayChoices()
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {SCORE}")

def displayChoices():
    global SCORE
    choiceA = random.choice(data)
    choiceB = random.choice(data)

    while choiceB == choiceA:
        choiceB = random.choice(data)

    print(f"Compare A: {choiceA['name']}, a {choiceA['description']}, from {choiceA['country']}.")
    print(vs)
    print(f"Compare B: {choiceB['name']}, a {choiceB['description']}, from {choiceB['country']}.")

    userChoice = input("Who has more followers? Type 'A' or 'B': ").lower()
    isRight = checkUserChoice(userChoice, choiceA['follower_count'], choiceB['follower_count'])
    if isRight:
        SCORE += 1
    else:
        return True

def checkUserChoice(userChoice, followA, followB):
    if followA > followB:
        return userChoice == 'a'
    else:
        return userChoice == 'b'

# Game
game()
