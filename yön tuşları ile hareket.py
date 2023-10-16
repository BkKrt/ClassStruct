from turtle import *
shape("turtle")
pensize(4)
win = Screen()
win.setup(500,500)

def solaDon():
    left(90)
    write("sola döndüm")
def sagaDon():
    right(90)
    write("sağa döndüm")
def ileri():
    forward(100)
def geri():
    backward(100)

win.onkeypress(solaDon,'Left')
win.onkeypress(sagaDon,'Right')
win.onkeypress(ileri,'Up')
win.onkeypress(geri,'Down')

win.listen()
win.mainloop()