import pandas as pd

natoPhoneticDataFrame = pd.read_csv("nato_phonetic_alphabet.csv")
studentNormalisationIndex = {value.letter: value.code for (index, value) in natoPhoneticDataFrame.iterrows()}

userInput = input(f"Enter a word: ")
userInputList = [letter.upper() for letter in userInput if letter.isalpha()]
nato = [phoneticWord for (letter, phoneticWord) in studentNormalisationIndex.items() if letter in userInputList]
print(" - ".join(word for word in nato))
