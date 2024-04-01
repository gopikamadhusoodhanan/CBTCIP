import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

def play(user_choice):
    computer_choice=random.choice(['Rock','Paper','Scissor'])
    if user_choice==computer_choice:
        result="It's tie"

    elif(user_choice=='rock' and computer_choice=='scissor') or\
        (user_choice=='paper' and computer_choice=='rock') or\
        (user_choice=='scissor' and computer_choice=='paper'):

        result="YOU WIN! Computer choose" + computer_choice
    else:
        result="YOU LOSE! Computer choose" + computer_choice
    messagebox.showinfo("Result",result)

root=tk.Tk()
root.title("Rock-Paper-Scissors Game")
print("Lets start!!")
rock_img=ImageTk.PhotoImage(Image.open("D:/inmakes python class/rock.png").resize((50, 50)))
paper_img=ImageTk.PhotoImage(Image.open("D:/inmakes python class/paper.png").resize((50, 50)))
scissors_img=ImageTk.PhotoImage(Image.open("D:/inmakes python class/scissors.png").resize((50, 50)))

rock_btn=tk.Button(root, text="Rock", width=100, image=rock_img,compound="left",command=lambda: play('rock'))
rock_btn.pack(pady=10)

paper_btn=tk.Button(root, text="Paper", width=100,image=paper_img,compound="left",command=lambda: play('paper'))
paper_btn.pack(pady=10)

scissors_btn=tk.Button(root, text="Scissors", width=100,image=scissors_img,compound="left",command=lambda: play('scissors'))
scissors_btn.pack(pady=10)

root.mainloop()

