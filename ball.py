from turtle import Turtle
from time import sleep


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.new_x = 0
        self.new_y = 0


    def move(self, x_dir, y_dir):
        self.new_x += x_dir
        self.new_y += y_dir
        sleep(0.01)
        self.goto(self.new_x, self.new_y)
