from replit import clear
from Data import MENU, resources, moneyReturn

# Global variables
MACHINE_CHOICES = ["espresso", "latte", "cappuccino"]
QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01


# Functions
def coffeeMachine():
    offMachine = False
    resources['money'] = 0
    while not offMachine:
        clear()
        userChoice = input("What would you like? (espresso|latte|cappuccino): ").lower()
        if "off" in userChoice:
            offMachine = True
        elif "report" in userChoice:
            displayResources()
        elif userChoice in MACHINE_CHOICES:
            MachineProcess(arg_userChoice=userChoice)
        else:
            print("Error input user.")


def displayResources():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}\n"
          f"Money: ${resources['money']}\n")


def MachineProcess(arg_userChoice):
    if checkResources(arg_userChoice=arg_userChoice):
        coin = float(input(f"insert ${MENU[arg_userChoice]['cost']} for a {arg_userChoice}"))
        if coin >= MENU[arg_userChoice]['cost']:
            if "espresso" in arg_userChoice:
                resources['water'] -= MENU[arg_userChoice]['ingredients']['water']
                resources['coffee'] -= MENU[arg_userChoice]['ingredients']['coffee']
            else:
                resources['water'] -= MENU[arg_userChoice]['ingredients']['water']
                resources['milk'] -= MENU[arg_userChoice]['ingredients']['milk']
                resources['coffee'] -= MENU[arg_userChoice]['ingredients']['coffee']
            resources['money'] += MENU[arg_userChoice]['cost']
            checkMoney(coin, MENU[arg_userChoice]['cost'])
            print(f"Here is ${moneyReturn['sum']} dollars in change.\n")
            print(f"Here is your {arg_userChoice}. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
            checkMoney(coin, MENU[arg_userChoice]['cost'])
            displayRefund()


def displayRefund():
    print(f"Quarters: {moneyReturn['quarters']}\n"
          f"Dimes:    {moneyReturn['dimes']}\n"
          f"Nickles:  {moneyReturn['nickles']}\n"
          f"Pennies:  {moneyReturn['pennies']}\n"
          f"Here is ${moneyReturn['sum']} dollars in change.\n")


def checkMoney(arg_coin, arg_cost):
    for index in moneyReturn:
        moneyReturn[index] = 0
    if arg_coin > arg_cost:
        remain = arg_coin - arg_cost
    else:
        remain = arg_coin
    while round(remain, 2) > 0:
        if round(remain - QUARTERS, 2) >= 0:
            moneyReturn['quarters'] += 1
            remain -= QUARTERS
        elif round(remain - DIMES, 2) >= 0:
            moneyReturn['dimes'] += 1
            remain -= DIMES
        elif round(remain - NICKLES, 2) >= 0:
            moneyReturn['nickles'] += 1
            remain -= NICKLES
        elif round(remain - PENNIES, 2) >= 0:
            moneyReturn['pennies'] += 1
            remain -= PENNIES
    moneyReturn['sum'] = round(((QUARTERS * moneyReturn['quarters']) +
                                (DIMES * moneyReturn['dimes']) +
                                (NICKLES * moneyReturn['nickles']) +
                                (PENNIES * moneyReturn['pennies'])), 2)


def checkResources(arg_userChoice):
    ingredients = MENU[arg_userChoice]['ingredients']
    isValid = True
    if "milk" in ingredients:
        for ingredient in ingredients:
            if resources[ingredient] < ingredients[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                isValid = False
    else:
        for ingredient in ingredients:
            if resources[ingredient] < ingredients[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                isValid = False
    return isValid


coffeeMachine()
