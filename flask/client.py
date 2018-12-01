from tkinter import *
from tree import *

master = Tk()
def clicked(event):
    print("clicked")

w = Canvas(master, width=2000, height=1000)
w.pack()
base_button = w.create_rectangle(0, 0, 100, 30, fill="grey40", outline="grey60")
base_txt = w.create_text(50, 15, text="Base")
branch_button = w.create_rectangle(0,0,100,100,fill="grey40", outline="grey60")
branch_txt = w.create_text()
w.tag_bind(base_button, "<Button-1>", clicked) ## when the square is clicked runs function "clicked".
w.tag_bind(base_txt, "<Button-1>", clicked) ## same, but for the text.
 #This function creates a base to be dragged
def genBase():
    w.create_rectangle()


mainloop()
