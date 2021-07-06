from paddle import Paddle
from scoreboard import ScoreBoard
from screen import PongScreen
from ball import Ball
from random import randint
pong_screen = PongScreen()
scoreboard = ScoreBoard()
user_paddle = Paddle(360, 0)
comp_paddle = Paddle(-360, 0)
pong_screen.screen.onkey(user_paddle.paddle_up, "Up")
pong_screen.screen.onkey(user_paddle.paddle_down, "Down")
pong_screen.screen.onkey(comp_paddle.paddle_up, "w")
pong_screen.screen.onkey(comp_paddle.paddle_down, "s")
ball = Ball()
x_dir = 4
y_dir = .3
while True:
    ball.move(x_dir, y_dir)
    if ball.ycor() > 280 or ball.ycor() < -280:
        y_dir = -y_dir
    elif ball.xcor() > 340:
        if ball.distance(user_paddle.xcor(), user_paddle.ycor()) < 80 and x_dir > 0:
            x_dir = -x_dir
            y_dir = y_dir + randint(0, 200)/100 - 1
        else:
            scoreboard.comp_point()
            ball.clear()
            ball.hideturtle()
            del ball
            ball = Ball()
    elif ball.xcor() < -340:
        if ball.distance(comp_paddle.xcor(), comp_paddle.ycor()) < 80 and x_dir < 0:
            x_dir = -x_dir
            y_dir = y_dir + randint(0, 200)/100 - 1
        else:
            scoreboard.user_point()
            ball.clear()
            ball.hideturtle()
            del ball
            ball = Ball()


pong_screen.screen.exitonclick()