from graphics import *

from random import randint
'''
The GraphWin is like a piece of paper.
If you want to draw anything, you need to make
a GraphWin object.

To make a GraphWin object, you must specify
a) name of the window
b) how many pixels wide it is
c) how many pixels high it is
'''

win = GraphWin('Rocks', 500, 500)
win.setBackground("pink")

'''
Every time you click the window, a circle
will appear where you clicked it.
'''

colors = ["red","orange","green", "turquoise", "purple", "yellow", "magenta",
          "grey","blue","white", "black"]
i = 0
while True:
    center_point = win.getMouse()
    c = Circle(center_point, randint(0,50))
    c.setFill(colors[i % len(colors)])
    c.draw(win)
    i = i + 1
