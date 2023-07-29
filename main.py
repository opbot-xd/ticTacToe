# imports
import tkinter as tk
import time
from boxes import Button
from functools import partial
from tkinter import font


# methods
def result(winner):
    for j in boxes:
        j.config(command=disable)
    resul_label=tk.Label(text='',font="serif 20 bold",bg="navajo white")
    if winner=='Draw':
        resul_label.config(text='Its a Dead Heat.',fg="gray15")
    elif winner=='Player 1':
        resul_label.config(text='Player 1 is the winner',fg="firebrick2")
    else:
        resul_label.config(text='Player 2 is the winner',fg="blue2")
    resul_label.place(anchor='center',rely=0.95,relx=0.5)
    screen.after(3500,screen.destroy)


def check():
    global winner
    text=[i.cget('text') for i in boxes]
    # x wins
    if text[0]==text[1]==text[2]=='X':
        winner="Player 1"
    if text[3]==text[4]==text[5]=='X':
        winner="Player 1"
    if text[6]==text[7]==text[8]=='X':
        winner="Player 1"
    if text[1]==text[4]==text[7]=='X':
        winner="Player 1"
    if text[0]==text[3]==text[6]=='X':
        winner="Player 1"
    if text[2]==text[5]==text[8]=='X':
        winner="Player 1"
    if text[0]==text[4]==text[8]=='X':
        winner="Player 1"
    if text[2]==text[4]==text[6]=='X':
        winner="Player 1"
    # O Wins.
    if text[0]==text[1]==text[2]=='O':
        winner="Player 2"
    if text[3]==text[4]==text[5]=='O':
        winner="Player 2"
    if text[6]==text[7]==text[8]=='O':
        winner="Player 2"
    if text[1]==text[4]==text[7]=='O':
        winner="Player 2"
    if text[0]==text[3]==text[6]=='O':
        winner="Player 2"
    if text[2]==text[5]==text[8]=='O':
        winner="Player 2"
    if text[0]==text[4]==text[8]=='O':
        winner="Player 2"
    if text[2]==text[4]==text[6]=='O':
        winner="Player 2"
    if "" not in text:
        winner = 'Draw'
    if winner!='':
        result(winner)

    
def disable():
    pass


def display(index):
    global turn
    active=boxes[index]
    if turn%2==0:
        active.config(text='X',fg='firebrick2')
    else:
        active.config(text='O',fg='blue2')
    active.config(command=disable)
    turn+=1
    check()


# setting the board
screen = tk.Tk()
screen.config(bg='navajo white')
screen.geometry('320x400')
screen.maxsize(320,400)
screen.minsize(320,400)
screen.title("Kattam-Katta")
icon = tk.PhotoImage(file="icon.png")
screen.iconphoto(False, icon)
intro1 = tk.Label(text="Player 1 - 'X'",font="impact 16 normal",bg="navajo white",fg="firebrick2")
intro1.place(anchor='center',rely=0.07,relx=0.25)
intro2 = tk.Label(text="Player 2 - '0'",font="impact 16 normal",bg="navajo white",fg="blue2")
intro2.place(anchor='center',rely=0.07,relx=0.75)
template = tk.PhotoImage(file="tic.png")
canvas=tk.Canvas(screen, width=300, height=300)
canvas.place(anchor="center",rely=0.5,relx=0.5)
canvas.create_image(150,150,anchor='center',image=template)
boxes=[]
for i in range(9):
    boxes.append((Button(canvas)).box)
row_column=(57,147,240,57,147,240,57,147,240)
for index,j in enumerate(boxes):
    if index in [0,1,2]:
        j.place(anchor='center',y=65,x=row_column[index])
    if index in [3,4,5]:
        j.place(anchor='center',y=150,x=row_column[index])
    if index in [6,7,8]:
        j.place(anchor='center',y=235,x=row_column[index])
    j.config(command=partial(display,boxes.index(j)))


# play
turn=0
winner=''
screen.mainloop()
