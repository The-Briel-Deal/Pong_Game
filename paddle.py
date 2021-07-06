from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=8)
        self.setheading(90)
        self.goto(x, y)


    def paddle_up(self):
        self.forward(10)

    def paddle_down(self):
        self.backward(10)
