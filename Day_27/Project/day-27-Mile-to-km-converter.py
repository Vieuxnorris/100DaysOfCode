from tkinter import *


# Function event
def convertMiles():
    correctInputList = [number for number in userInput.get() if number.isdigit()]
    correctInputFloat = float("".join(number for number in correctInputList))
    correctInput = correctInputFloat * 1.609344
    resultConvertLabel.config(text=f"{round(correctInput, 6)}")


# Screen
window = Tk()
window.title("Mile to km converter")
window.minsize(width=400, height=100)
window.config(padx=100, pady=10)

# Entry
userInput = Entry(width=10)
userInput.grid(column=1, row=0)

# Labels
milesLabel = Label(text="Miles", font=("Arial", 10))
milesLabel.grid(column=2, row=0)
milesLabel.config(padx=5)

infoLabel = Label(text="is equal to ", font=("Arial", 10))
infoLabel.grid(column=0, row=1)

resultConvertLabel = Label(text="0", font=("Arial", 10))
resultConvertLabel.grid(column=1, row=1)

kmLabel = Label(text="Km", font=("Arial", 10))
kmLabel.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=convertMiles)
button.grid(column=1, row=2)

window.mainloop()
