from art import logo
from replit import clear
import random

# Fonctions
def distribution(playerDict):
    for numberPlayer in range(2):
        emptyPlayer = {}
        emptyPlayer['card'] = [random.choice(cardValeurs), random.choice(cardValeurs)]
        emptyPlayer['total'] = emptyPlayer['card'][0] + emptyPlayer['card'][1]
        playerDict.append(emptyPlayer)

def checkBlackjack(entity):
    if entity['total'] == 21:
        entity['blackjack'] = True
    else:
        entity['blackjack'] = False

def checkOver(entity):
    if entity['total'] > 21:
        entity['over'] = True
    else:
        entity['over'] = False

def checkWin(player, computer, verifBlackjack):
    if computer['blackjack'] == True and len(computer['card']) < 3:
        print(f"     Your final hand: {player['card']}, final score: {player['total']}")
        print(f"     Computer final hand: {computer['card']}, final score: 0")
        print("Lose, opponent has Blackjack 😱")
        return True
    elif player['blackjack'] == True and len(player['card']) < 3:
        print(f"     Your final hand: {player['card']}, final score: 0")
        print(f"     Computer final hand: {computer['card']}, final score: {computer['total']}")
        print("Win with a Blackjack 😎")
        return True
    elif player['over'] == True:
        print(f"     Your final hand: {player['card']}, final score: {player['total']}")
        print(f"     Computer final hand: {computer['card']}, final score: {computer['total']}")
        print("You went over. You lose 😭")
        return True
    elif computer['over'] == True:
        print(f"     Your final hand: {player['card']}, final score: {player['total']}")
        print(f"     Computer final hand: {computer['card']}, final score: {computer['total']}")
        print("Opponent went over. You win 😁")
        return True
    elif player['total'] < computer['total'] and verifBlackjack == False:
        print(f"     Your final hand: {player['card']}, final score: {player['total']}")
        print(f"     Computer final hand: {computer['card']}, final score: {computer['total']}")
        print("You lose 😤")
        return True
    elif player['total'] > computer['total'] and verifBlackjack == False:
        print(f"     Your final hand: {player['card']}, final score: {player['total']}")
        print(f"     Computer final hand: {computer['card']}, final score: {computer['total']}")
        print("You win 😀")
        return True
    elif player['total'] == computer['total'] and verifBlackjack == False:
        print(f"     Your final hand: {player['card']}, final score: {player['total']}")
        print(f"     Computer final hand: {computer['card']}, final score: {computer['total']}")
        print("Draw 🙃")
        return True              

def anotherCard(player):
    newCard = random.choice(cardValeurs)
    if newCard == 11:
        newCard = 1
    player['card'].append(newCard)
    total = 0
    for n in range(len(player['card'])):
        total += player['card'][n]
    player['total'] = total


# Variables
cardValeurs = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 10 ,10, 10, 11]
playerDict = []
playGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

# Game
clear()
while 'y' in playGame:
    print(logo)

    playerDict = []
    endGame = False

    distribution(playerDict)
    while endGame != True:
        for entity in playerDict:
            checkBlackjack(entity)
            checkOver(entity)

        player = playerDict[0]
        computer = playerDict[1]

        print(f"     Your cards: {player['card']}, current score: {player['total']}")
        print(f"     Computer's first card: {computer['card'][0]}")

        endGame = checkWin(player, computer, True)
        if endGame != True:
            playerChoice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if 'y' in playerChoice:
                anotherCard(player)
            else:
                while computer['total'] < 17:
                    anotherCard(computer)
                    checkOver(computer)
                endGame = checkWin(player, computer, False)
        




    playGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    clear()