from tkinter import *
from datetime import datetime

root = Tk()
root.title('Stopwatch')
root.geometry('400x400')
root.resizable(width=False, height=False)


temp = 0
after_id = ''

def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
    clock_label.configure(text=str(f_temp))
    temp += 1


def start_tick():
    tick()

def stop_tick():
    root.after_cancel(after_id)

def continue_tick():
    tick()

def reset_tick():
    global temp
    temp = 0
    clock_label.configure(text='00:00')





clock_label = Label(root, text='00:00', bg='black', fg='white', font=("Open Sans MS", 45, "bold"))
clock_label.place(relx=0.5, rely=0.15, anchor='center')

btn_start = Button(root, text="Start" ,font=("Open Sans MS", 30), bg="black", fg="black", width=5, command=start_tick)
btn_start.place(relx=0.5, rely=0.45, anchor='center')


btn_continue = Button(root, text="Continue" ,font=("Open Sans MS", 30), bg="black", fg="black", width=5, command=continue_tick)
btn_continue.place(relx=0.5, rely=0.60, anchor='center')

btn_stop = Button(root, text="Stop" ,font=("Open Sans MS", 30), bg="black", fg="black", width=5, command=stop_tick)
btn_stop.place(relx=0.5, rely=0.75, anchor='center')

btn_reset = Button(root, text="Reset" ,font=("Open Sans MS", 30), bg="black", fg="black", width=5, command=reset_tick)
btn_reset.place(relx=0.5, rely=0.9, anchor='center')






root.mainloop()