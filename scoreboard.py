from turtle import Turtle


class ScoreBoard:
    def __init__(self):
        self.comp_score = Turtle()
        self.comp_score.color("white")
        self.comp_score.penup()
        self.comp_score.hideturtle()
        self.comp_score.goto(70, 270)
        self.comp_score.score = 0
        self.comp_score.write(arg=self.comp_score.score, move=False, align="center", font=("Arial", 20, "normal"))
        self.user_score = Turtle()
        self.user_score.color("white")
        self.user_score.penup()
        self.user_score.hideturtle()
        self.user_score.goto(-70, 270)
        self.user_score.score = 0
        self.user_score.write(arg=self.user_score.score, move=False, align="center", font=("Arial", 20, "normal"))

    def comp_point(self):
        self.comp_score.score += 1
        self.comp_score.clear()
        self.comp_score.write(arg=self.comp_score.score, move=False, align="center", font=("Arial", 20, "normal"))

    def user_point(self):
        self.user_score.score += 1
        self.user_score.clear()
        self.user_score.write(arg=self.user_score.score, move=False, align="center", font=("Arial", 20, "normal"))
