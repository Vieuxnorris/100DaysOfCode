from tkinter import *

# Global Variables

window = Tk()
window.title("My first GUI program")
window.minsize(width=800, height=600)
window.config(padx=200, pady=100)


# Label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
#my_label.pack(side="left")
#my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

# Modif option
my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button

def button_click():
    my_label.config(text=input.get())


button = Button(text="Click me", command=button_click)
#button.pack()
button.grid(column=1, row=1)

# new Button
button = Button(text="new Button")
button.grid(column=2, row=0)


# Entry

input = Entry(width=10)
#input.pack()
input.grid(column=3, row=2)

window.mainloop()
