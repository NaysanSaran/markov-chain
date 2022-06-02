from cProfile import label
from calendar import c
from re import T
import numpy as np 
import tkinter as tk
from tkinter import *
import tkinter.font
import tkinter.ttk as ttk
from tkinter import messagebox
# Import the MarkovChain class from markovchain.py
from markovchain import MarkovChain


root = Tk()  
root.wm_geometry("800x600+0+0")
root.wm_title("UP to 4x4 Markov Chain Draw") 
root.focus_set()
root.grab_set()

row_col = StringVar()
#row_col.set("3")


win0 = Frame(root)
win1 = Frame(root)
frame1 = Frame(win1)

def drawModel():
    #M = np.column_stack(rows)
    #mc = MarkovChain(M, ['A', 'B', 'C', 'D'])
    #mc.draw()
    M = np.zeros((int(row_col.get()),int(row_col.get())))
    cols = []
    rows = []
    for i in range(0,int(row_col.get())):
        for j in range(0,int(row_col.get())):
            widget = frame1.grid_slaves(row=i, column=j)[0].get()
            cols.append(widget)
            #M.append(widget)
            #print(widget)
            #print(M[i][j])
        rows.append(cols)
        cols = []
    #print (rows)
    M = np.vstack(rows)
    print(f'Type(a) = {type(M)}.  a = {M}')
    mc = MarkovChain(M, ['1', '2', '3'])
    mc.draw("../img/markov-chain-tree-states.png")    
    
#    messagebox.showinfo('Message', 'You clicked the Submit button!')

def callback(row_col):
    cont = int(row_col.get()) + 0
    if cont >= 2 and  cont <= 4:
        for widget in frame1.winfo_children():
            widget.destroy()
        for j in range(int(row_col.get())):
            for i in range(int(row_col.get())):
                e = Entry(frame1,width=10,font=myFont,bd=5)
                e.grid(row=i, column=j, sticky=NSEW)
                frame1.pack()
        frame1.pack()
    else:
        messagebox.showinfo('Message', 'Please enter a number between 2 and 4')

myFont = tkinter.font.Font(family = 'Helvetica' , size = 12, weight = 'bold')
win0.pack(side="top", fill="both", expand=True)
label0 = Label(win0, text="Draw MDP from transition Matrix", font=myFont)
label0.pack(side="top", fill="both", expand=True)

win1.pack(side="top", fill="both", expand=True)
photo = PhotoImage(file = "markov.png")
w = Label(win1, image=photo)
w.pack()
lblRows = Label(win1, text="Rows & cols :", font=myFont)
lblRows.pack(side=TOP)
row_col.trace("w", lambda name, index, mode, row_col=row_col: callback(row_col))
e1 = Entry(win1, bd =5, width=10, textvariable=row_col)
#e1.insert(0,row_col.get())
e1.pack(side=TOP)
label1 = Label(win1, text="Transition Matrix :", font=myFont)
label1.pack(side=TOP)

win2 = Frame(root)
win2.pack(side="top", fill="both", expand=True)
label2 = Label(win2, text="Enter the state labels:", font=myFont)
label2.pack()
buttonDraw = Button(win2, text = "Draw!", font = myFont, command=lambda: drawModel(), bg = 'light blue', height = 2 ,width = 8)
buttonDraw.pack()
root.mainloop()