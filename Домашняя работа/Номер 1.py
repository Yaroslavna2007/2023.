from tkinter import *
import time

r = Tk()
r.title('Ball')

c = Canvas(r, width = 250, height = 250)
c.pack()

ball1 = c.create_oval(10, 10, 20, 20,fill = 'yellow')

while True:
    for i in range(30):
        c.move(ball1, 1 , 0)
        time.sleep(0.02)
        r.update()
    for i in range(30):
        c.move(ball1, -1 , 0)
        time.sleep(0.02)
        r.update()

