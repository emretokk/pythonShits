from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text="Clicked the button")
	myLabel.pack()

myButton = Button(root, text="Clickkkk", padx=50, pady=25, command=myClick, fg="blue", bg="#000000")#state=DISABLED)
myButton.pack()

root.mainloop()