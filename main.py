from turtle import Screen
from ball import Ball
from paddle import Paddle
from items import Items
from score import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")

while True:
    ball = Ball()
    paddle = Paddle()
    items = Items()
    score = ScoreBoard()

    screen.listen()
    screen.onkey(paddle.move_paddle_right, "Right")
    screen.onkey(paddle.move_paddle_left, "Left")

    y = 0
    i = 0
    colors = ["yellow", "yellow", "green", "green", "orange", "orange", "red", "red"]
    for _ in range(1, 9):
        for x in range(-300, 350, 50):
            items.create_item(x, y, colors[i])
        y += 25
        i += 1


    game = True
    while game:
        time.sleep(ball.speed)
        screen.update()
        ball.move_ball()

        for item in items.items:
            if ball.distance(item) < 30:
                if ball.ycor() > item.ycor():
                    ball.bounce_x()
                elif ball.ycor() < item.ycor():
                    ball.bounce_y()
                item.hideturtle()
                items.items.remove(item)

        if ball.ycor() < -300:
            game = False

        if ball.ycor() > 300:
            score.update_score(1)
            score.update_scoreboard()
            game = False

        if ball.xcor() > 300:
            ball.bounce_x()

        if ball.xcor() < -300:
            ball.bounce_x()

        if 100 >= paddle.xcor() - ball.xcor() >= -100 and ball.ycor() < -290:
            ball.bounce_y()

screen.exitonclick()
