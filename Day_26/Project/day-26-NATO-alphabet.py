import pandas as pd

nato = []

natoPhoneticDataFrame = pd.read_csv("nato_phonetic_alphabet.csv")
studentNormalisationIndex = {value.letter: value.code for (index, value) in natoPhoneticDataFrame.iterrows()}

userInput = input(f"Enter a word: ")
userInputList = [letter.upper() for letter in userInput if letter.isalpha()]

for letter in userInputList:
    nato += [word for (natoLetters, word) in studentNormalisationIndex.items() if natoLetters == letter]

print(" - ".join(word for word in nato))
