from tkinter import *


root = Tk()
root.title("Clicker")
root.geometry("200x200")
root.resizable(width=False, height=False)

count = 0
Click = Label(root, text="0", font=("Open Sans MS", 35, "bold"))
message = Label(root, text="", font=('Times New Roman', 20, 'italic'))
Click.pack()
message.place(x=50, y=70)

def clicked():
    global count
    count += 1
    Click.configure(text=str(count))
    if count == 10:
        message.configure(text=f"{count}")


Click_button = Button(
    root,
    text="Click",
    font=("Open Sans MS", 20, "bold"),
    bg="black",
    fg="black",
    command= clicked
)
Click_button.place(x=60, y=100)


root.mainloop()