# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

playerChose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computerChose = random.randint(0,2)

choseList = [rock, paper, scissors]

print(f"{choseList[playerChose]}\n Computer chose: {choseList[computerChose]}")
if (playerChose > 2 or playerChose < 0):
    print("Error")
elif (playerChose == 0 and computerChose == 2):
    print("You win")
elif (playerChose == 2 and computerChose == 1):
    print("You win")
elif (playerChose == 1 and computerChose == 0):
    print("You win")
elif (playerChose == computerChose):
    print("Equality")
else:
    print("You lose")