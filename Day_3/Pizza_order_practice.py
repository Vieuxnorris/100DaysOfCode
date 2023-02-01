# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

small = 15
medium = 20
large = 25

pepperoniSmall = 2
pepperoniMediumLarge = 3

Extra = 1

if size == 'S':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            print(f"Your final bill is: ${small + pepperoniSmall + Extra}.")
        else:
            print(f"Your final bill is: ${small + pepperoniSmall}.")
    else:
        if extra_cheese == 'Y':
            print(f"Your final bill is: ${small + Extra}.")
        else:
            print(f"Your final bill is: ${small}.")

elif size == 'M':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            print(f"Your final bill is: ${medium + pepperoniMediumLarge + Extra}.")
        else:
            print(f"Your final bill is: ${medium + pepperoniMediumLarge}.")
    else:
        if extra_cheese == 'Y':
            print(f"Your final bill is: ${medium + Extra}.")
        else:
            print(f"Your final bill is: ${medium}.")

elif size == 'L':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            print(f"Your final bill is: ${large + pepperoniMediumLarge + Extra}.")
        else:
            print(f"Your final bill is: ${large + pepperoniMediumLarge}.")
    else:
        if extra_cheese == 'Y':
            print(f"Your final bill is: ${large + Extra}.")
        else:
            print(f"Your final bill is: ${large}.")