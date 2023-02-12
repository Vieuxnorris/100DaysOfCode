# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def readNamesLetters():
    with open("./Input/Names/invited_names.txt", "r") as file:
        readLines = file.readlines()
        for index in range(len(readLines)-1):
            readLines[index] = readLines[index].strip('\n')
        return readLines


def replaceTemplate(arg_name):
    templateText = []
    with open("./Input/Letters/starting_letter.txt", "r") as file:
        templateText = file.readlines()
        templateText[0] = templateText[0].replace("[name]", arg_name)

    with open(f"./Output/ReadyToSend/Letter_for_{arg_name}.txt", "w") as file:
        file.writelines(templateText)


listNames = readNamesLetters()
for name in listNames:
    replaceTemplate(name)
