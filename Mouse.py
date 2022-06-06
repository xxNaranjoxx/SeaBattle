from tkinter import *

def display_coordinates(event):
    if event.x <= 40:
        print("hola")

win = Tk()
can = Canvas(win, width=400, height=400, background="white")
can.bind("<Button-1>", display_coordinates)
can.grid(row=0,column=0)

win.mainloop()
