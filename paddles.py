from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.userAttrs = {
            "color" : "white",
            "shape" : "square",
            "width" : 20,
            "height" :100
            }
        self.shape(self.userAttrs["shape"])
        self.penup()
        self.color(self.userAttrs["color"])
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def movePaddleUp(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def movePaddleDown(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)