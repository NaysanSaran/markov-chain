import numpy as np 
import tkinter as tk
from tkinter import *
import tkinter.font
import tkinter.ttk as ttk
# Import the MarkovChain class from markovchain.py
from markovchain import MarkovChain

root = Tk()

root.wm_geometry("420x400+0+0")
root.wm_title("UP to 4x4 Markov Chain Draw") 
root.focus_set()
root.grab_set()

myFont = tkinter.font.Font(family = 'Helvetica' , size = 12, weight = 'bold')

photo = PhotoImage(file = "2.png")
w = Label(root, image=photo)

def drawModel(rows, cols):
    
    M = np.column_stack(rows)
    mc = MarkovChain(M, ['A', 'B', 'C', 'D'])
    mc.draw()
    
def getmatrix():
    for row in rows:
        for col in row:
            m = col.get()
            print(m)

rows = []
for i in range(4):
    cols = []
    for j in range(4):
        e = Entry(root,width=10,font=myFont,bd=5)
        e.grid(row=i, column=j, sticky=NSEW)
        cols.append(e)
    rows.append(cols)
    
print("cols : ", cols)
print("rows : ", rows)
root.mainloop()
#draw = Button(root, text = "Draw",
#                 font = myFont, bd=4, command = drawModel(rows, cols) ,
#                 bg = 'light blue', height = 2 ,width = 8)
#draw.grid(row=5, column=2)