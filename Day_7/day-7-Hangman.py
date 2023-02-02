import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

word = random.choice(word_list).lower()
wordLen = len(word)
lives = 6
endGame = False

blankWord = []
tempoLetter = []

for n in range(wordLen):
    blankWord.append("_")

print(f"Pssst, the solution is {word}")

while not endGame:
    guessLetter = input("Guess a letter: ").lower()
    if guessLetter not in tempoLetter:
      tempoLetter.append(guessLetter)
    elif guessLetter in tempoLetter:
      print(f"This letter is already use : {'-'.join(tempoLetter)}")

    for index in range(wordLen):
      letter = word[index]
      # print(f"Current position: {index}\n Current letter: {letter}\n Guessed letter: {guessLetter}")
      if letter == guessLetter:
        blankWord[index] = letter

    if guessLetter not in word:
      print(f"This letter made you lose a life : {guessLetter}")
      lives -= 1
      if lives == 0:
        endGame = True
        print("You lose.")

    print(f"{' '.join(blankWord)}")
    print(stages[lives])

    if "_" not in blankWord:
      endGame = True
      print("You win.")

