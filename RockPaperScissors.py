import random
import tkinter as tk
from tkinter import messagebox

user_wins =0
computer_wins=0
def play(user_choice):
    options = ['rock','paper','scissors']

    computer_choice = random.choice(options)   

    #Choices are the same
    if computer_choice == user_choice:
        result = "Tie!"

    elif(user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'paper' and computer_choice == 'rock') or \
        (user_choice == 'scissors' and computer_choice == 'paper'):
            result = 'You win!'
    else:
         result = 'Computer wins'

    messagebox.showinfo("Result", f"You chose {user_choice}\n Computer chose {computer_choice}\n{result}")


    






# UI setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x300")

tk.Label(root, text="Rock Paper Scissors!",font=("Helvetica",20,"bold")).pack(pady=20)
tk.Label(root, text="Choose your move:",font=("Helvetica",14,"bold")).pack(pady=1)

tk.Button(root, text="Rock", command=lambda: play("rock")).pack(pady=5)
tk.Button(root, text="Paper", command=lambda: play("paper")).pack(pady=5)
tk.Button(root, text="Scissors", command=lambda: play("scissors")).pack(pady=5)

root.mainloop()
