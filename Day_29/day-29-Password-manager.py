import random
from tkinter import *

# Global Variables
WIDTH_SCREEN = 500
HEIGHT_SCREEN = 400
WIDTH_LOGO = 200
HEIGHT_LOGO = 200
EXCEPTION = [34, 39, 46, 44]
MAX_LONG_PASSWORD = 20


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    randomPassword = [chr(alphabet) for alphabet in range(97, 123)] + \
                     [chr(ponctuation) for ponctuation in range(33, 65) if ponctuation not in EXCEPTION] + \
                     [chr(maj) for maj in range(65, 90)]
    random.shuffle(randomPassword)
    passwordEntry.delete(0, END)
    passwordEntry.insert(END, "".join(letter for letter in randomPassword[0:MAX_LONG_PASSWORD]))


# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePassword():
    if len(websiteEntry.get()) != 0 and len(emailUsernameEntry.get()) != 0 and len(passwordEntry.get()) != 0:
        with open("save_password.txt", "a") as file:
            file.write(f"{websiteEntry.get()} | {emailUsernameEntry.get()} | {passwordEntry.get()}\n")
        websiteEntry.delete(0, END)
        emailUsernameEntry.delete(0, END)
        passwordEntry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Screen
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=WIDTH_LOGO, height=HEIGHT_LOGO, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(WIDTH_LOGO / 2, HEIGHT_LOGO / 2, image=logo)
canvas.grid(column=1, row=0)

# Labels
websiteLabel = Label(text="website:", pady=10, padx=10)
websiteLabel.grid(column=0, row=1)
emailUsernameLabel = Label(text="Email/Username:", pady=10, padx=10)
emailUsernameLabel.grid(column=0, row=2)
passwordLabel = Label(text="Password:", pady=10, padx=10)
passwordLabel.grid(column=0, row=3)

# Entry
websiteEntry = Entry(width=50)
websiteEntry.grid(column=1, row=1, columnspan=2)
emailUsernameEntry = Entry(width=50)
emailUsernameEntry.grid(column=1, row=2, columnspan=2)
passwordEntry = Entry(width=30)
passwordEntry.grid(column=1, row=3)

# Buttons
generatorPassword = Button(text="Generate password", command=generator)
generatorPassword.grid(column=2, row=3)
addButton = Button(text="Add", width=42, command=savePassword)
addButton.grid(column=1, row=4, columnspan=2)

# Mainloop
window.mainloop()
