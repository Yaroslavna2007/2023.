from tkinter import *
import time
import random

class Ball:
    def __init__(self, canvas, x1, y1, x2, y2, speed, xDir, yDir):
        self.canvas = canvas
        self.speed = speed
        self.ball = canvas.create_oval(x1, y1, x2, y2)
        self.xDir = xDir
        self.yDir = yDir

    def showId(self):
        print(self.ball)

    def move(self):
        self.canvas.move(self.ball, self.speed * self.xDir, self.speed * self.yDir)
        c = self.canvas.coords(self.ball)
        if c[0] <= 0:
            self.xDir = 1
        elif c[2] >= 500:
            self.xDir = -1
        if c[3] >= 500:
            self.yDir = -1
        elif c[1] <= 0:
            self.yDir = 1

root = Tk()
root.title("Balls")

canvas = Canvas(root, width = 500, height = 500)
canvas.pack()

x = random.randint(20, 100)
ball1 = Ball(canvas, 250, 10, 260, 20, 10, -1, -1)
ball2 = Ball(canvas, 260, 40, 280, 60, 8, 1, -1)
ball3 = Ball(canvas, 300, 80, 380, 160, 7, 1, -1)

while True:
    ball1.move()
    ball2.move()
    ball3.move()
    time.sleep(0.02)
    root.update()
