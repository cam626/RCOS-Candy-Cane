from tkinter import *
from tree import *
from client_communications import *

import random
import json

master = Tk()
canv = Canvas(master, width=2000, height=1000)
canv.pack()
placing = "None"

def placeRedOrnament(event):
    canv.tag_bind(drawing_section, "<Button-1>", placeRed)

def placeGreenOrnament(event):
    canv.tag_bind(drawing_section, "<Button-1>", placeGreen)

def placeBlueOrnament(event):
    canv.tag_bind(drawing_section, "<Button-1>", placeBlue)

def placeRed(event):
    canv.create_oval(event.x_root-100,event.y_root-100,event.x_root-50,event.y_root-50,fill="red",outline="black")
    canv.tag_unbind(drawing_section, "<Button-1>")

def placeGreen(event):
    canv.create_oval(event.x_root-100,event.y_root-100,event.x_root-50,event.y_root-50,fill="green",outline="black")
    canv.tag_unbind(drawing_section, "<Button-1>")

def placeBlue(event):
    canv.create_oval(event.x_root-100,event.y_root-100,event.x_root-50,event.y_root-50,fill="blue",outline="black")
    canv.tag_unbind(drawing_section, "<Button-1>")

def placeBranch(event):
    canv.tag_bind(drawing_section,"<Button-1>",placeB)


def placeB(event):
    canv.create_rectangle(event.x_root-100,event.y_root-45,event.x_root-10,event.y_root-50,fill="green",outline="black")
    canv.tag_unbind(drawing_section,"<Button-1>")
    sendBranch(treeID, "green", event.x_root, event.y_root, 90, 5)

# lights
def placeRedlight(event):
    canv.tag_bind(drawing_section, "<Button-1>", placeRedL)

def placeGreenlight(event):
    canv.tag_bind(drawing_section, "<Button-1>", placeGreenL)

def placeBluelight(event):
    canv.tag_bind(drawing_section, "<Button-1>", placeBlueL)

def placeRedL(event):
    canv.create_oval(event.x_root-67,event.y_root-60,event.x_root-62,event.y_root-53,fill="red",outline="black")
    canv.tag_unbind(drawing_section, "<Button-1>")

def placeGreenL(event):
    canv.create_oval(event.x_root-67,event.y_root-60,event.x_root-62,event.y_root-53,fill="green",outline="black")
    canv.tag_unbind(drawing_section, "<Button-1>")

def placeBlueL(event):
    canv.create_oval(event.x_root-67,event.y_root-60,event.x_root-62,event.y_root-53,fill="blue",outline="black")
    canv.tag_unbind(drawing_section, "<Button-1>")




#Drawing all the buttons

branch_button = canv.create_rectangle(0,30,100,60,fill="grey40", outline="grey60")
branch_txt = canv.create_text(50,45,text="Branch")
topper_button = canv.create_rectangle(0,60,100,90,fill="grey40",outline="grey60")
topper_txt = canv.create_text(50,75,text="Topper")
#ORNAMENT OPTIONS
ornament_button = canv.create_rectangle(0,90,100,120,fill="grey40",outline="grey60")
ornament_txt = canv.create_text(50,105,text="Blue Ornament")
ornament_red = canv.create_rectangle(0,120,100,150,fill="grey40",outline="grey60")
ornament_red_txt = canv.create_text(50,135,text="Red Ornament")
ornament_green = canv.create_rectangle(0,150,100,180,fill="grey40",outline="grey60")
ornament_green_txt = canv.create_text(50,165,text="Green Ornament")
#ORNAMENT OPTIONS DONE
light_button = canv.create_rectangle(0,180,100,210,fill="grey40",outline="grey60")
light_txt = canv.create_text(50,195,text="Red Lights")
light_green = canv.create_rectangle(0,210,100,240,fill="grey40",outline="grey60")
light_green_txt = canv.create_text(50,225,text="Green Lights")
light_blue = canv.create_rectangle(0,240,100,270,fill="grey40",outline="grey60")
light_blue_txt = canv.create_text(50,255,text="Blue Lights")
#trunk_button = canv.create_rectangle(0,225,100,255,fill="grey40",outline="grey60")
#trunk_txt = canv.create_text(50,225,text="Trunk")

drawing_section = canv.create_rectangle(100, 0, 1900, 1000, fill="white")

#Done drawing, now onto binding all of them to functions
canv.tag_bind(ornament_button, "<Button-1>", placeBlueOrnament)
canv.tag_bind(ornament_txt, "<Button-1>", placeBlueOrnament)
canv.tag_bind(ornament_red, "<Button-1>", placeRedOrnament)
canv.tag_bind(ornament_red_txt, "<Button-1>", placeRedOrnament)
canv.tag_bind(ornament_green, "<Button-1>", placeGreenOrnament)
canv.tag_bind(ornament_green_txt, "<Button-1>", placeGreenOrnament)

#Binding the lights
canv.tag_bind(light_button, "<Button-1>", placeRedlight)
canv.tag_bind(light_txt, "<Button-1>", placeRedlight)
canv.tag_bind(light_blue, "<Button-1>", placeBluelight)
canv.tag_bind(light_blue_txt, "<Button-1>", placeBluelight)
canv.tag_bind(light_green, "<Button-1>", placeGreenlight)
canv.tag_bind(light_green_txt, "<Button-1>", placeGreenlight)

#Binding the branch
canv.tag_bind(branch_button, "<Button-1>", placeBranch)
canv.tag_bind(branch_txt, "<Button-1>", placeBranch)

 #This function creates a base to be dragged
canv.create_rectangle(1000,300,1020,600,fill="brown",outline="black")
def genBase():
    canv.create_rectangle()


mainloop()
