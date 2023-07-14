from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.setposition(-80, 250)
        self.color("white")
        self.update_scoreboard()

    def update_score(self, number):
        self.score += number

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}",
                   move=False, font=('Courier New', 40, 'normal'))

    def game_over(self):
        self.clear()
        self.setposition(-275, 0)
        self.write(f"Game Over! Your score is {self.score}", move=False,
                   font=('Courier New', 20, 'normal'))
