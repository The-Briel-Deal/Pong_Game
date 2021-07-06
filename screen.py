from turtle import Screen


class PongScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(800, 600)
        self.screen.bgcolor("black")
        self.screen.delay(0)
        self.screen.listen()
