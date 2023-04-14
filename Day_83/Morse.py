import pandas as pd

def openCsv(file):
    data = pd.read_csv(file)
    dictData = {value.letter: value.morse for (index, value) in data.iterrows()}
    return dictData



if __name__ == '__main__':
    morseData = openCsv('morse.csv')
    phrase = input("Enter your message in Morse:")

    output = [morseData.get(letter.upper()) for letter in phrase]

    print(f"{' '.join(output)}")


