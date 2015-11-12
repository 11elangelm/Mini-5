# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 22:42:55 2015

@author: Kevin
"""

#from Tkinter import *
#import time
#
#
#root = Tk()
#canv = Canvas(root, highlightthickness=0)
#canv.pack(fill='both', expand=True)
#top = canv.create_line(0, 0, 640, 0, fill='green', tags=('top'))
#left = canv.create_line(0, 0, 0, 480, fill='green', tags=('left'))
#right = canv.create_line(639, 0, 639, 480, fill='green', tags=('right'))
#bottom = canv.create_line(0, 478, 640, 478, fill='red', tags=('bottom'))
#
#rect = canv.create_rectangle(270, 468, 365, 478, outline='black', fill='gray40', tags=('rect'))
#ball = canv.create_oval(0, 20, 20, 40, outline='black', fill='gray40', tags=('ball'))
#
#
#
#def moveit(obj,x,y):
#    canv.move(obj,x,y)
#    time.sleep(0.05)
#    
#for i in range(100):
#    moveit(ball,1,2)
#    root.update()
##    time.sleep(0.05)   
#
#    
#    
##root.resizable(0, 0)
#root.mainloop()


from Tkinter import *

import math

c = Canvas(width=200, height=200)
c.pack()

# a square
xy = [(50, 50), (150, 150)]
#Cancha.create_line(x,y,x+r*math.cos(a),y+r*math.sin(a), fill = "white", width = 5)
polygon_item = c.create_line(xy)

center = 100, 100

def getangle(event):
    dx = c.canvasx(event.x) - center[0]
    dy = c.canvasy(event.y) - center[1]
    try:
        return complex(dx, dy) / abs(complex(dx, dy))
    except ZeroDivisionError:
        return 0.0 # cannot determine angle

def press(event):
    # calculate angle at start point
    global start
    start = getangle(event)

def motion(event):
    # calculate current angle relative to initial angle
    global start
    angle = getangle(event) / start
    offset = complex(center[0], center[1])
    newxy = []
    for x, y in xy:
        v = angle * (complex(x, y) - offset) + offset
        newxy.append(v.real)
        newxy.append(v.imag)
        
    print newxy
    c.coords(polygon_item, *newxy)

c.bind("<Button-1>", press)
c.bind("<B1-Motion>", motion)

mainloop()

