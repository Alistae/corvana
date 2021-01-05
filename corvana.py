import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("300x100")
root.title("CORVANA")
title = tk.Label(root, text="CORVANA", font="courier 40 bold")
title.pack()
e1 = tk.Entry(root)
e1.pack()

def dataentry(event):
    data=e1.get()
    data=data[:-1]
    e1.delete(0, END)
    if data in ("what projects do i have", "what are my projects", "projects", "current projects", "list my projects"):
        with f as open("projects.txt", "r"):
            f.read()

root.bind("<Return>", dataentry)
tk.mainloop()
