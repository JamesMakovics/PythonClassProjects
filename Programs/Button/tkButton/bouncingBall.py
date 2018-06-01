from tkinter import *
import time

WIDTH = 800
HEIGHT = 500
SIZE = 50
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()
color = 'red'


class Ball:
    def __init__(self):
        self.shape = canvas.create_oval(0, 0, SIZE, SIZE, fill=color)
        '''
        self.shape1 = canvas.create_arc(0, 0, SIZE, SIZE, fill = color, start=self.position(0), extent = self.position(200))
        self.shape2 = canvas.create_arc(0, 0, SIZE, SIZE, fill = color, start=self.position(200), extent = self.position(400))
        '''
        self.speedx = 9 # changed from 3 to 9
        self.speedy = 9 # changed from 3 to 9
        self.active = True
        self.move_active()

    def position(self,n):
        return 360.0 * n / 1000

    def ball_update(self):
        canvas.move(self.shape, self.speedx, self.speedy)
        pos = canvas.coords(self.shape)
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.speedx *= -1
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.speedy *= -1

    def move_active(self):
        if self.active:
            self.ball_update()
            tk.after(40, self.move_active) # changed from 10ms to 30ms

ball = Ball()
tk.mainloop()