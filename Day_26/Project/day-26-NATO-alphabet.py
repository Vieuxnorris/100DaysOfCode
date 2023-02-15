import pandas as pd

# Variables
nato = []

# Core
natoPhoneticDataFrame = pd.read_csv("nato_phonetic_alphabet.csv")
NormalisationIndex = {value.letter: value.code for (index, value) in natoPhoneticDataFrame.iterrows()}

userInput = input(f"Enter a word: ")
userInputList = [letter.upper() for letter in userInput if letter.isalpha()]

for letter in userInputList:
    nato += [word for (natoLetters, word) in NormalisationIndex.items() if natoLetters == letter]

print(" - ".join(word for word in nato))
