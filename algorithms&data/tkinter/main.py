from tkinter import *
from tkinter import ttk







                                                #BEGIN
# root = Tk()
# root.title("Testing Application")
# root.geometry("600x400")
# root.resizable(width=False, height=False)
# root.iconbitmap("img/icon.ico")
#
# root.config(bg="black")
# # root['bg'] = 'red'
#
# def output():
#     print("Hello")
#
#
# btn = Button(root,
#              text="Кнопка",
#              command=output,
#              font=("Comic Sans MS", 20, "bold"),
#              width=4,
#              height=2,
#              highlightbackground='lime',
#              activebackground='red',
#              activeforeground='white',
#              fg='red'
#              )
#
# label_1 = Label(
#     root,
#     text="Some label",
#     font=("Open Sans MS", 25, "italic"),
#     bg="lime",
#     fg="red",
# )
#
# img_1 = PhotoImage(file="img/mash.png")
# l_logo = Label(root, image=img_1,)
#
# label_1.pack(padx=15,pady=15)
# btn.pack()
# l_logo.pack()
#
#
#
#
# root.mainloop()


# from tkinter import *
# from random import randint
#
# root = Tk()
# root.title("Rock Paper Scissor")
# root.geometry("600x400")
# root.resizable(width=False, height=False)
# root['bg'] = "black"
#
# labelText = Label(root, text="")
#
#
#
#
#
#
# root.mainloop()












                                                #BUTTONS




# from tkinter import *
#
# root = Tk()
# root.title("Application")
# root.geometry("400x400")
# root.resizable(width=False, height=False)
#
# e = Entry(root, width=30,)
# e.pack()
#
#
# # def add():
# #     e.insert(END,"Hello")
# #
# def delete():
#     e.delete(0,END)
# #
# # def get():
# #     label_1['text'] = e.get()
#
# def add():
#     e.insert(END, "1 ")
#
# def get():
#     number = list(int(i) for i in e.get().split())
#     result = sum(number)
#     try:
#         average = result / len(number)
#     except ZeroDivisionError as error:
#         str = f"You cant divide by zero: {error}"
#         print(str)
#         label_1['text'] = str
#         return
#     label_1['text'] = f"sum = {result}, count = {len(number)}, average_grade = {round(average,3)}"
#
#
#
#
#
#
# btn_1 = Button(
#     root,
#     font=("Open Sans MS", 20, "bold"),
#     bg="black",
#     fg="black",
#     text="Insert",
#     command=add,
# )
# btn_1.pack()
#
# btn_2 = Button(
#     root,
#     font=("Open Sans MS", 20, "bold"),
#     bg="black",
#     fg="black",
#     text="Delete",
#     command=delete,
# )
#
# btn_2.pack()
#
# btn_3 = Button(
#     root,
#     font=("Open Sans MS", 20, "bold"),
#     bg="black",
#     fg="black",
#     text="Get",
#     command=get,
# )
#
# btn_3.pack()
#
#
#
# label_1 = Label(root, bg="white", fg="black", font=('Open Sans MS', 15, 'bold'))
# label_1.pack()
#
#
#
#
#
# root.mainloop()









                                                # LABEL

# root = Tk()
# root.title("Computer")
# root.geometry("500x500")
# root.resizable(width=False, height=False)
# root['bg']="black"
#
# # l1 = Label(root, text="1" ,bg="white", fg="black", font=("Open Sans MS", 15, "bold"), width=8, height=4).pack()
# # l2 = Label(root, text="2" ,bg="green", fg="white", font=("Open Sans MS", 15, "bold"), width=8, height=4).pack(expand=1, anchor=E)
# # l3 = Label(root, text="3" ,bg="yellow", fg="black", font=("Open Sans MS", 15, "bold"), width=8, height=4).pack(expand=1, fill=Y)
# # l4 = Label(root, text="4" ,bg="blue", fg="white", font=("Open Sans MS", 15, "bold"), width=8, height=4).pack()
# # l4 = Label(root, text="5" ,bg="red", fg="black", font=("Open Sans MS", 15, "bold"), width=8, height=4).pack(side = BOTTOM)
#
# label1 = Label(root, text="Hello!", fg="white", bg="green", padx=10, pady=10)
# label1.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.5, relheight=0.5)
#
# root.mainloop()


# from functools import reduce
#
# words = ["Python", "reduce", "function", "accumulate", "transformation"]
#
# longest_word = reduce(lambda a,b: a if len(a) > len(b) else b, words)
#
# print(f"longest word: {longest_word}")


