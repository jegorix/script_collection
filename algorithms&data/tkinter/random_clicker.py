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


def tick_timer():
    pass




def start_game():
    global clicks
    clicks = 0
    LabelClick.configure(text=str(clicks))
    btn_click.place(relx=0.5, rely=0.3, anchor=CENTER)
    btn_start.place_forget()
    tick_timer()
    change_pos()



def end_game():
    pass




LabelClick = Label(root, text='0', font=("Comis Sans MS", 40, "bold"), bg="black", fg="white")
LabelClick.place(relx=0.5, rely=0.1, anchor=CENTER)

btn_click = Button(root, font=("Comis Sans MS", 25, "bold"), text="Click", bg="white", fg="black", padx=15, pady=10, command = change_pos)
btn_start = Button(root, font=("Comis Sans MS", 25, "bold"), text="Start", bg="white", fg="black", padx=15, pady=10, command = start_game)
btn_start.place(relx=0.5, rely=0.4, anchor=CENTER)

timer_label = Label(root, text="00:00:00", font=("Comic Sans MS", 30, "bold"), bg="black", fg="white")
timer_label.place(relx=0.07, rely=0.07, anchor=CENTER)


root.mainloop()