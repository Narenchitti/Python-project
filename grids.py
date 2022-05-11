from tkinter import *

root = Tk()

mylabel1 = Label(root, text="Hello world")
mylabel2 = Label(root, text="AVM python")

mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=0)

root.mainloop()
