from turtle import Turtle, Screen
import time
from paddles import Paddle
from ball import Ball


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
ball = Ball()


# Listen keys
screen_object.listen()
screen_object.onkey(user1_paddle.movePaddleUp,"Up")
screen_object.onkey(user1_paddle.movePaddleDown,"Down")
screen_object.onkey(user2_paddle.movePaddleUp,"w")
screen_object.onkey(user1_paddle.movePaddleDown,"s")


game_on = True
while game_on:
    screen_object.update()



screen_object.exitonclick()
