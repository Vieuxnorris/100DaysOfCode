from art import logo
from replit import clear

calculatorDict = {
    "operators": ['+', '-', '*', '/'],
    "calcul":{
        'a':0,
        'b':0,
    },
    "result":0,
}

def addition(a, b):
    """
        return a + b
    """
    return a + b

def sustraction(a,b):
    """
        return a - b
    """
    return a - b

def multiplication(a,b):
    """
        return a * b
    """
    return a * b

def division(a,b):
    """
        return a / b
    """
    return a / b

continueCalcul = 'y'
print(logo)

while True:
    if 'n' in continueCalcul:
        clear()
        calculatorDict['result'] = 0
        print(logo)
    
    if calculatorDict['result'] == 0:
        calculatorDict["calcul"]['a'] = float(input("What's the first number?: "))

    for operator in calculatorDict['operators']:
        print(operator)

    operator = input("Pick on operation: ")
    if operator not in calculatorDict['operators']:
        print("Error operator")
    else:
        calculatorDict["calcul"]['b'] = float(input("What's the next number?: "))

        if operator == '+':
            calculatorDict['result'] = addition(calculatorDict["calcul"]['a'], calculatorDict["calcul"]['b'])
        elif operator == '-':
            calculatorDict['result'] = sustraction(calculatorDict["calcul"]['a'], calculatorDict["calcul"]['b'])
        elif operator == "*":
            calculatorDict['result'] = multiplication(calculatorDict["calcul"]['a'], calculatorDict["calcul"]['b'])
        else:
            calculatorDict['result'] = division(calculatorDict["calcul"]['a'], calculatorDict["calcul"]['b'])

        a = calculatorDict["calcul"]['a']
        b = calculatorDict["calcul"]['b']
        print(f"{a} {operator} {b} = {calculatorDict['result']}")

        calculatorDict['calcul']['a'] = calculatorDict['result']
        continueCalcul = input(f"Type 'y' to continue calculating with {calculatorDict['result']}, or type 'n' to start a new calculation: ").lower()
