

from curses import window
import tkinter
from turtle import width


w=400
h = 400
window = tkinter.Tk()
tkinter.Canvas.size(w)
window.mainloop()

while 1==1:
    x = 1
    print(1)
    x + 1



import time
from turtle import *
color('blue', 'green')
startdur = 0
duration = 100
f = 40
l = 5
r = 10
b = 30
begin_fill()
speed(1000)
while startdur <= 100:
    startdur + 1
    forward(f)
    left(l)
    right(r)
    back(b)
    color('red')
    circle(30)
    color('blue')
    f = f+ .5
    l = l+ .5
    r = r + .5
    b = b+ .5
    forward(f)
    left(l)
    right(r)
    back(b)
    
    f = f * 1.00314
    l = l * 1.00314
    r = r  * 1.00314
    b = b* 1.00314
