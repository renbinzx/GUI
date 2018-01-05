from Tkinter import *
import sys

def button():
    top = tk.Tk()
    Button = tk.Button(top,text = 'Quit',command = sys.exit)
    Button.grid()    
    top.mainloop()

def label():
    top1 = Toplevel()
    top2 = Toplevel(top1)
    top1.title('Parent')
    top2.title('son')
    label = Label(top1,text = "Hello, World!")
    label2 = Label(top2, text = "Hello")
    label.config(bg = "#000000", fg = "yellow",height = 3, width = 20)
    label.config(relief = RIDGE)
    label2.pack()
    label.pack(expand = YES,fill = BOTH)
    top1.mainloop()
