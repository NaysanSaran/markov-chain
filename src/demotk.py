from cProfile import label
import numpy as np 
import tkinter as tk
from tkinter import *
import tkinter.font
import tkinter.ttk as ttk
from tkinter import messagebox
# Import the MarkovChain class from markovchain.py
from markovchain import MarkovChain

def drawModel():
    #M = np.column_stack(rows)
    #mc = MarkovChain(M, ['A', 'B', 'C', 'D'])
    #mc.draw()
    messagebox.showinfo('Message', 'You clicked the Submit button!')
    #return 0


root = Tk()  
root.wm_geometry("800x600+0+0")
root.wm_title("UP to 4x4 Markov Chain Draw") 
root.focus_set()
root.grab_set()

myFont = tkinter.font.Font(family = 'Helvetica' , size = 12, weight = 'bold')
win0 = Frame(root)
win0.pack(side="top", fill="both", expand=True)
label0 = Label(win0, text="Enter the transition matrix:", font=myFont)

win1 = Frame(root)
win1.pack(side="top", fill="both", expand=True)
label1 = Label(win1, text="Enter the transition matrix:", font=myFont)
label1.pack()
photo = PhotoImage(file = "markov.png")
w = Label(win1, image=photo)
w.pack()


frame1 = Frame(win1)
for j in range(4):
    for i in range(4):
        e = Entry(frame1,width=10,font=myFont,bd=5)
        e.grid(row=i, column=j, sticky=NSEW)
        frame1.pack()
#e = Entry(frame1,width=10,font=myFont,bd=5)
#e.grid(row=0, column=1, sticky=NSEW)
#e1 = Entry(frame1,width=10,font=myFont,bd=5)
#e1.grid(row=0, column=2, sticky=NSEW)
frame1.pack()

win2 = Frame(root)
win2.pack(side="top", fill="both", expand=True)
label2 = Label(win2, text="Enter the state labels:", font=myFont)
label2.pack()
buttonDraw = Button(win2, text = "Draw!", font = myFont, command=lambda: drawModel(), bg = 'light blue', height = 2 ,width = 8)
buttonDraw.pack()
root.mainloop()