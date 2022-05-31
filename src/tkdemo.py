import numpy as np 
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font
import tkinter.ttk as ttk
# Import the MarkovChain class from markovchain.py
from markovchain import MarkovChain

tk = Tk()


tk.wm_geometry("680x600+0+0")
tk.wm_title("UP to 4x4 Markov Chain Draw") 

label = ttk.Label(tk, text="UP to 4x4 Markov Chain Draw"
                 , font=("Helvetica", 16),
                 foreground = "white", background = "black"
                 )
label.pack()
tk.focus_set()
tk.grab_set()
tk.mainloop()