from turtle import Turtle
import random

directionsx = [-1,1]
directionsy = [0]
updatey = [-10, -5, 5, 10]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ballAttrs = {
            "shape" : "circle",
            "color" : "white",
            "posx" : 0,
            "posy" : 0
        }
        self.move_x = 10
        self.move_y = 10
        self.shape(self.ballAttrs["shape"])
        self.penup()
        self.color(self.ballAttrs["color"])
        self.goto(self.ballAttrs["posx"],self.ballAttrs["posy"])
        self.randomdirectionx = random.choice(directionsx)
        self.randomdirectiony = random.choice(directionsy)
        self.move_x *= self.randomdirectionx
        self.move_y *= self.randomdirectiony

    def moveBall(self):
        x = self.xcor() + self.move_x
        y = self.ycor() + self.move_y
        self.goto(x,y)

    def reverty(self):
        self.move_y *= -1

    def revertx(self):
        self.move_x *= -1

    def reball(self):
        self.home()

    def checky(self):
        if self.move_y == 0:
            return True
        else:
            return False
    
    def update(self):
        self.move_y += random.choice(updatey)
