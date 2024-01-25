# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 15:34:42 2022

@author: Alikinda
"""

import tkinter as tk
import time
start_time = time.time()
pressed = False
count = 0
t=0
t1=0
p=0
p1=0

def pressed(event):
    global pressed
    global p
    pressed = True
    p = time.time() - start_time
    #print("button pushed at", t)
    
def released(event):
    global pressed
    global p
    pressed = False
    p1 = time.time() - start_time
    #print("button released at", t1)
    print("button held down for", p1-p, "seconds")
    
def click():
    global count
    global t
    global t1
    if count == 0:
        print(count +1)
        #records time of first button press
        t = time.time() - start_time
        #Shows the user the "start"
        print(t-t)
    elif count <= 3:
        print(count +1)
        #records time of button presses past the first one
        t1 = time.time() - start_time
        #shows the user the difference between the "start" and the current button press
        print(t1-t)
    elif count == 4:
        #after the 4th press, it stops calculating and prints this.
        print('button pressed four times')
        #as well as removes the keypad to avoid excessive inputs
        root.destroy()
    count += 1



root = tk.Tk()
root.title("gui button")

btn = tk.Button(root, text="button", command = click)

btn.pack()

btn.bind('<ButtonPress-1>',pressed)

btn.bind('<ButtonRelease-1>',released)

root.mainloop()