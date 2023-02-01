# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lowerName1 = name1.lower()
lowerName2 = name2.lower()

trueName1 = lowerName1.count('t') + lowerName1.count('r') + lowerName1.count('u') + lowerName1.count('e')
loveName1 = lowerName1.count('l') + lowerName1.count('o') + lowerName1.count('v') + lowerName1.count('e')

trueName2 = lowerName2.count('t') + lowerName2.count('r') + lowerName2.count('u') + lowerName2.count('e')
loveName2 = lowerName2.count('l') + lowerName2.count('o') + lowerName2.count('v') + lowerName2.count('e')

trueSum = str(trueName1 + trueName2)
loveSum = str(loveName1 + loveName2)

trueLoveSum = int(trueSum + loveSum)

if trueLoveSum < 10 or trueLoveSum > 90:
    print(f"Your score is {trueLoveSum}, you go together like coke and mentos.")
elif trueLoveSum > 40 and trueLoveSum < 50:
    print(f"Your score is {trueLoveSum}, you are alright together.")
else:
    print(f"Your score is {trueLoveSum}.")