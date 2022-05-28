import numpy as np 
import tkinter as tk
from tkinter import *
# Import the MarkovChain class from markovchain.py
from markovchain import MarkovChain

def main():
    
    a=a11.get()
    b=a12.get()
    c=a21.get()
    d=a22.get()
    P = np.array([[a, b], [c, d]]) # Transition matrix
    mc = MarkovChain(P, ['A', 'B'])
    mc.draw()

def tkinter():
    global a11
    global a12
    global a21
    global a22

    root = Tk()
    root.title('2 X 2 Transition Matrix')
    photo = PhotoImage(file = "2.png")
    w = Label(root, image=photo)
    w.pack()

    label1=Label(root,text='A 11 :' ,bg='#33FF93')
    label1.pack()

    a11 = DoubleVar()
    ent = Entry(root,textvariable=a11)
    ent.pack()
    ent.grid(row=0,column=0)

    label2=Label(root,text='A 12 :' ,bg='#33FF93')
    label2.pack()

    a12 = DoubleVar()
    ent2 = Entry(root,textvariable=a12)
    ent2.pack()
    ent2.grid(row=0,column=1)

    label3=Label(root,text='A 21 :' ,bg='#33FF93')
    label3.pack()

    a21 = DoubleVar()
    ent3 = Entry(root,textvariable=a21)
    ent3.pack()
    ent3.grid(row=1,column=0)

    label4=Label(root,text='A 22 :' ,bg='#33FF93')
    label4.pack()

    a22 = DoubleVar()
    ent4 = Entry(root,textvariable=a22)
    ent4.pack()
    ent4.grid(row=1,column=1)


    button = Button(root,bg="#FF5833",fg="#ecf0f1",font=("cala"),text="Draw",justify="center", command=main)
    button.pack()



    root.mainloop()

tkinter()
