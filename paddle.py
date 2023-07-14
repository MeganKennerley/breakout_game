from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_len=10)
        self.penup()
        self.setposition(x=(0, -300))
        self.speed("fastest")

    def move_paddle_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def move_paddle_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
