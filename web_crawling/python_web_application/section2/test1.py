from tkinter import *

# Making a simple GUI Tool
def printHello():
    print('Hi!')

root = Tk()
w = Label(root, text='Python test')
b = Button(root, text='Hello, Python', command = printHello)
c = Button(root, text='Quit', command=root.quit)

w.pack()
b.pack()
c.pack()

root.mainloop()
