from tkinter import *
from tree import *
import random
master = Tk()
canv = Canvas(master, width=2000, height=1000)
canv.pack()
placing = "None"
#Function responsible for drawing the trunk


def drawTrunk(event):
    random_x = random.randint(400,1600)
    random_y = random.randint(100,700)
    rect = canv.create_rectangle(random_x,random_y,random_x+30,random_y+100,fill="brown",outline="brown")

def placeOrnament(event):
    print("Sup bitch")
    canv.tag_bind(drawing_section, "<Button-1>", place)

def place(event):
    print(placing)
    canv.create_oval(event.x_root-100,event.y_root-100,event.x_root-50,event.y_root-50,fill="red",outline="black")
    print(event.x_root,event.y_root)
    canv.tag_unbind(drawing_section, "<Button-1>")



#Drawing all the buttons
base_button = canv.create_rectangle(0, 0, 100, 30, fill="grey40", outline="grey60")
base_txt = canv.create_text(50, 15, text="Base")
branch_button = canv.create_rectangle(0,30,100,60,fill="grey40", outline="grey60")
branch_txt = canv.create_text(50,45,text="Branch")
topper_button = canv.create_rectangle(0,60,100,90,fill="grey40",outline="grey60")
topper_txt = canv.create_text(50,75,text="Topper")
#ORNAMENT OPTIONS
ornament_button = canv.create_rectangle(0,90,100,120,fill="grey40",outline="grey60")
ornament_txt = canv.create_text(50,105,text="Blue Ornament")
ornament_red = canv.create_rectangle(0,120,100,150,fill="grey40",outline="grey60")
ornament_red_txt = canv.create_text(50,135,text="Red Ornament")
ornament_green = canv.create_rectangle(0,150,100,180,fill="grey40",outline="grey40")
ornament_green_txt = canv.create_text(80,165,text="Green Ornament")
#ORNAMENT OPTIONS DONE
#lights_button = canv.create_rectangle(0,195,100,225,fill="grey40",outline="grey60")
#lights_txt = canv.create_text(50,195,text="Lights")
#trunk_button = canv.create_rectangle(0,225,100,255,fill="grey40",outline="grey60")
#trunk_txt = canv.create_text(50,225,text="Trunk")

drawing_section = canv.create_rectangle(100, 0, 1900, 1000, fill="white")

#Done drawing, now onto binding all of them to functions
canv.tag_bind(ornament_button, "<Button-1>", placeOrnament)
canv.tag_bind(ornament_txt, "<Button-1>", placeOrnament)
 #This function creates a base to be dragged
def genBase():
    canv.create_rectangle()


mainloop()
