from art import logo
from replit import clear

action = {}

def addPerson(name, bill):
    action[name] = bill

def checkWinAction():
    maxBill = 0
    winAction = ""
    for key in action:
        if action[key] > maxBill:
            maxBill = action[key]
            winAction = key
    print(f"The winner is {winAction} with a bid of ${maxBill}.")

print(logo)
print("Welcome to the secret auction program")

finalUser = False

while finalUser is not True:
    name = input("What is your name?: ")
    bill = int(input("What's your bill?: $"))
    addPerson(name=name, bill=bill)

    addUser = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if "no" in addUser:
        finalUser = True

    clear()

checkWinAction()