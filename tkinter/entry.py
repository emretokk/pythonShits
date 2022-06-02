from tkinter import *

root = Tk()

e = Entry(root, width=100, borderwidth=5)
e.pack()
# e.insert(0, "Enter your name") inserts the input as a default


def myClick():
	hello = "Hello " + e.get()
	myLabel = Label(root, text=hello)
	myLabel.pack()

myButton = Button(root, text="Enter Your Name", padx=50, pady=25, command=myClick, fg="blue", bg="#000000")#state=DISABLED)
myButton.pack()

root.mainloop()