import numpy as np 
import tkinter as tk
from tkinter import *
import tkinter.font
import tkinter.ttk as ttk
# Import the MarkovChain class from markovchain.py
from markovchain import MarkovChain

root = Tk()

root.wm_geometry("800x600+0+0")
root.wm_title("UP to 4x4 Markov Chain Draw") 
root.focus_set()
root.grab_set()

titleFont = tkinter.font.Font(family = 'Helvetica' , size = 14, weight = 'bold')
regularFont = tkinter.font.Font(family = 'Helvetica' , size = 12, weight = 'bold')
photo = PhotoImage(file = "markov.png")
frm_main = Frame(root)
frm_main.pack(side="top", fill="both", expand=True)
w = Label(frm_main, image=photo)
w.pack()

def drawModel(rows, cols):
    
    M = np.column_stack(rows)
    #mc = MarkovChain(M, ['A', 'B', 'C', 'D'])
    #mc.draw()
    
def getmatrix():
    frame = Frame(root)
    frame.pack(side=TOP)
    for row in rows:
        for col in row:
            m = col.get()

rows = []
for i in range(4):
    cols = []
    for j in range(4):
        e = Entry(root,width=10,font=myFont,bd=5)
        e.pack(side=LEFT)
        #e.grid(row=i, column=j, sticky=NSEW)
        cols.append(e)
    rows.append(cols)
label = Label(root, text="Enter the transition matrix:", font=myFont)
label.pack()
#print("cols : ", cols)
#print("rows : ", rows)
draw = Button(root, text = "Draw",
                 font = myFont, bd=4, command = drawModel(rows, cols) ,
                 bg = 'light blue', height = 2 ,width = 8)
#draw.pack(row=5, column=2)
draw.pack()
root.mainloop()
