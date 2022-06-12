from turtle import Turtle

class Paddle:
    def __init__(self):
        self.attrs1 = {
            "color" : "white",
            "shape" : "square",
            "width" : 20,
            "height" :100,
            "x_pos" : 350,
            "y_pos" : 0}

        self.attrs2 = {
            "color" : "white",
            "shape" : "square",
            "width" : 20,
            "height" :100,
            "x_pos" : -350,
            "y_pos" : 0}
        self.paddles = []
        self.createPaddle1()
        self.createPaddle2()
    
    def createPaddle1(self):
        newPaddle=Turtle(shape=self.attrs1["shape"])
        newPaddle.penup()
        newPaddle.color(self.attrs1["color"])
        newPaddle.shapesize(stretch_wid=5, stretch_len=1)
        newPaddle.goto(self.attrs1["x_pos"],self.attrs1["y_pos"])
        self.paddles.append(newPaddle)

    def createPaddle2(self):
        newPaddle=Turtle(shape=self.attrs2["shape"])
        newPaddle.penup()
        newPaddle.color(self.attrs2["color"])
        newPaddle.shapesize(stretch_wid=5, stretch_len=1)
        newPaddle.goto(self.attrs2["x_pos"],self.attrs2["y_pos"])
        self.paddles.append(newPaddle)