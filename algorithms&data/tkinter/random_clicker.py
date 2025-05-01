from tkinter import *
from tkinter import messagebox
from random import random

clicks = 0

root = Tk()
root.title("Random Clicker")
root.geometry("1280x720")
root.resizable(width=False, height=False)
root["bg"] = "black"


def change_pos():
    global clicks
    clicks += 1
    LabelClick.configure(text=str(clicks))
    btn_click.place(relx=random(), rely=random(), anchor=CENTER)






LabelClick = Label(root, text='0', font=("Comis Sans MS", 40, "bold"), bg="black", fg="white")
LabelClick.place(relx=0.5, rely=0.1, anchor=CENTER)

btn_click = Button(root, font=("Comis Sans MS", 25, "bold"), text="Click", bg="white", fg="black", padx=15, pady=10, command = change_pos)
btn_click.place(relx=0.5, rely=0.3, anchor=CENTER)



root.mainloop()