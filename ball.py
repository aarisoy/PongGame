from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ballAttrs = {
            "shape" : "circle",
            "color" : "white",
            "posx" : 0,
            "posy" : 0
        }
        self.shape(self.ballAttrs["shape"])
        self.penup()
        self.color(self.ballAttrs["color"])
        self.goto(self.ballAttrs["posx"],self.ballAttrs["posy"])