from tkinter import *

root = Tk()

# Creating label widget

myLabel1 = Label(root, text="Hello World")#.grid(row=0, column=0)
myLabel2 = Label(root, text="Keops")#.grid(row=1, column=0)

# Shoving it onto the screen

# myLabel1.pack()
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)


root.mainloop()