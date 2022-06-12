from turtle import Turtle, Screen
import time
from paddles import Paddle


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

paddles = Paddle()
screen_object.update()







screen_object.exitonclick()
