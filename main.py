from turtle import Screen
from paddle import Paddle
import time

LEFT_PADDLE_STARTING_POSITION = (-350, 0)
RIGHT_PADDLE_STARTING_POSITION = (350, 0)

# how ofter the screen renders in seconds - higher is slower
GAME_SPEED = 0.08

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Python Pong")

# Stops the screen from performing its normal rendering and animations
screen.tracer(0)

left_paddle = Paddle(LEFT_PADDLE_STARTING_POSITION)
right_paddle = Paddle(RIGHT_PADDLE_STARTING_POSITION)

screen.listen()
screen.onkeypress(left_paddle.start_up, "w")
screen.onkeypress(left_paddle.start_down, "s")
screen.onkeyrelease(left_paddle.stop, "w")
screen.onkeyrelease(left_paddle.stop, "s")

screen.onkeypress(right_paddle.start_up, "Up")
screen.onkeypress(right_paddle.start_down, "Down")
screen.onkeyrelease(right_paddle.stop, "Up")
screen.onkeyrelease(right_paddle.stop, "Down")

game_running = True
while game_running:
    screen.update()
    time.sleep(GAME_SPEED)
    left_paddle.move()
    right_paddle.move()

screen.exitonclick()