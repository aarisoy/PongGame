from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.user1_score = 0
        self.user2_score = 0
        self.goto(-100,200)
        self.write(self.user1_score,move=False, align="center",font=("Courier", 50, "normal"))
        self.goto(100,200)
        self.write(self.user2_score,move=False, align="center",font=("Courier", 50, "normal"))

    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.user1_score,move=False, align="center",font=("Courier", 50, "normal"))
        self.goto(100,200)
        self.write(self.user2_score,move=False, align="center",font=("Courier", 50, "normal"))

    def hit(self, x):
        if x > 0:
            self.user1_score += 1
            self.update()
        else:
            self.user2_score += 1
            self.update()

    def announcement(self):
        if self.user1_score == 5:
            self.goto(0,0)
            self.write("Game is over. Winner is right paddle.", move=False, align="center", font=("Courier", 20, "normal"))
        if self.user2_score == 5:
            self.goto(0,0)
            self.write("Game is over. Winner is left paddle.", move=False, align="center", font=("Courier", 20, "normal"))