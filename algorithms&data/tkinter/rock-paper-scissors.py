from tkinter import *
from random import choice

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("600x400")
root.resizable(width=False, height=False)
root['bg'] = "black"


def compare_choices(computer_choice, player_choice):
    if player_choice == computer_choice:
        return 'Draw'

    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        return 'You Win'
    else:
        return 'You Lose'





def why_rps(player_choice):
    rps = ['Rock', 'Paper', 'Scissors']
    computer_choice = choice(rps)
    result = compare_choices(computer_choice, player_choice)
    labelText.configure(text=f"Computer choice: {computer_choice}\n{result}")





labelText = Label(root, text="", fg="white", font=("Comic Sans MS", 20, "italic"), bg='black')
labelText.place(y=150, x=200)

rock = Button(root,
              text="Rock",
              font=('Open Sans MS', 20),
              bg="white",
              command=lambda: why_rps("Rock")
              )
rock.place(x=100, y=300)


scissors = Button(root,
              text="scissors",
              font=('Open Sans MS', 20),
              bg="white",
              command=lambda: why_rps("Scissors")
              )
scissors.place(x=200, y=300)


paper = Button(root,
              text="paper",
              font=('Open Sans MS', 20),
              bg="white",
              command=lambda: why_rps("Paper")
              )
paper.place(x=330, y=300)






root.mainloop()