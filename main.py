from turtle import Turtle, Screen
import time
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard


# Definitions for screen setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = "black"
TITLE = "PongGame by Alpay"

# Create screen object
screen_object = Screen()

# Configure screen
screen_object.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen_object.bgcolor(BACKGROUND_COLOR)
screen_object.title(TITLE)
screen_object.tracer(0)

# Create paddle object
user1_paddle = Paddle((350,0))
user2_paddle = Paddle((-350,0))

# Create ball object
ball = Ball()

# Create scoreboard object
scoreboard = Scoreboard()

# Listen keys
screen_object.listen()
screen_object.onkeypress(user1_paddle.movePaddleUp,"Up")
screen_object.onkeypress(user1_paddle.movePaddleDown,"Down")
screen_object.onkeypress(user2_paddle.movePaddleUp,"w")
screen_object.onkeypress(user2_paddle.movePaddleDown,"s")


game_on = True
while game_on:
    screen_object.update()
    time.sleep(0.04)
    
    ball.moveBall()
    if abs(ball.ycor()) > 280:
        ball.reverty()
    
    if ball.distance(user1_paddle) < 55 and ball.xcor() > 340:
        ball.revertx()
        if ball.checky() == True:
            ball.update()

    elif ball.distance(user2_paddle) < 55 and ball.xcor() < -340:
        ball.revertx()
        if ball.checky() == True:
            ball.update()
    
    elif abs(ball.xcor()) > 340:
        scoreboard.hit(ball.xcor())
        ball.reball()
        ball.revertx()

    if scoreboard.user1_score == 5 or scoreboard.user2_score == 5:
        scoreboard.announcement()
        game_on = False   


screen_object.exitonclick()
