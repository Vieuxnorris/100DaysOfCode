from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from replit import clear

def coffeeMachine():
    offMachine = False
    machineMenu = Menu()
    machineMaker = CoffeeMaker()
    machineMoney = MoneyMachine()
    while not offMachine:
        clear()
        userChoice = input(f"What would you like? {machineMenu.get_items()}: ").lower()
        drink = machineMenu.find_drink(userChoice)
        if userChoice == "off":
            offMachine = True
        elif userChoice == "report":
            machineMaker.report()
            machineMoney.report()
        elif drink is not None:
            if machineMaker.is_resource_sufficient(drink):
                if machineMoney.make_payment(drink.cost):
                    machineMaker.make_coffee(drink)


coffeeMachine()
