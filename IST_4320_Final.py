import random
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
import os


main = tk.Tk() 
main.title("Magic 8 BALL")

a = tk.StringVar() 
b = tk.StringVar()          
possibleResponses = ["It is certain",
    "Reply hazy, try again",
    "Don’t count on it",
    "It is decidedly so",
    "Ask again later",
    "My reply is no",
    "Without a doubt",
    "Better not tell you now",
    "My sources say no",
    "Yes definitely",	
    "Cannot predict now",	
    "Outlook not so good",
    "You may rely on it",	
    "Concentrate and ask again",	
    "Very doubtful",
    "As I see it, yes",		
    "Most likely",		
    "Outlook good",		
    "Yes",		
    "Signs point to yes"]

label_name = tk.Label(main, text="What would you like to know?", font=('helvetica',14,'bold'))
name_entry = tk.Entry(main, textvariable = a, font=('calibre',14,'normal'))
 


def showResponse():
    popup = tk.Toplevel(main)
    popup.title("Popup Window!")
    popup_label = tk.Label(popup, text=getResponse(), font=('calibre',14,'normal'))
    popup_label.pack()

   
def randomNumber(x):
    import random
    return random.randint(1, x)

def getResponse():
    return possibleResponses[randomNumber(20) - 1]



submit_button = tk.Button(main,
    text="Submit",
    font=('calibre',14,'normal'),
    command = showResponse)


label_name.pack()
name_entry.pack()
submit_button.pack()
main.mainloop()