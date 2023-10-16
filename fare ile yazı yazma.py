from turtle import*
pensize(3)
win = Screen()
win.setup(800,800)
penup()

def Nokta(x,y):
    goto(x,y)
    pendown()
win.onclick(Nokta)
mainloop()