from turtle import Turtle


class Items(Turtle):

    def __init__(self):
        super().__init__()
        self.items = []

    def create_item(self, x, y, color):
        new_item = Turtle("square")
        new_item.shapesize(stretch_len=2)
        new_item.penup()
        new_item.color(color)
        new_item.speed("fastest")
        new_item.goto(x, y)
        self.items.append(new_item)




