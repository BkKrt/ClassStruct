from turtle import *
import time
w=Screen()
w.setup(300,700)
w.title("Trafik ışığı uygulaması")

penup()
goto(0,180)
pendown()
pensize(4)

for i in range(2):
    forward(80)
    right(90)
    forward(220)
    right(90)
def kirmizi():
    penup()
    goto(40,140)
    fillcolor("red")
    shape("circle")
    shapesize(3)

def sari():
    penup()
    goto(40,70)
    fillcolor("yellow")
    shape("circle")
    shapesize(3)
    
def yeşil():
    penup()
    goto(40,0)
    fillcolor("green")
    shape("circle")
    shapesize(3)
stop_loop = False

def stop():
    # stop_loop değişkenini global olarak tanımlayın
    global stop_loop
    # stop_loop değişkenini True olarak ayarlayın
    stop_loop = True

# 'q' tuşuna basıldığında stop fonksiyonunu çağırın
w.onkeypress(stop, 'q')
w.listen()

while True:
    kirmizi()
    time.sleep(5)
    
    if stop_loop:
        break
    sari()
    time.sleep(2)
    
    if stop_loop:
        break
    yeşil()
    time.sleep(3)
    
    if stop_loop:
        break
    

w.mainloop()  