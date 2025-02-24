from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

LEFT_PADDLE_STARTING_POSITION = (-350, 0)
RIGHT_PADDLE_STARTING_POSITION = (350, 0)

BALL_MAX_HEIGHT = 280
BALL_MIN_HEIGHT = -280
BALL_MAX_WIDTH = 410
BALL_MIN_WIDTH = -410

# how ofter the screen renders in seconds - higher is slower
GAME_SPEED = 0.05

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Python Pong")

# Stops the screen from performing its normal rendering and animations
screen.tracer(0)

# Create paddles and setup key listeners for their movement
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

# Create ball
ball = Ball()

game_running = True
while game_running:
    screen.update()
    time.sleep(GAME_SPEED)

    left_paddle.move()
    right_paddle.move()

    next_ball_x = ball.xcor() + ball.x_speed * ball.x_direction
    next_ball_y = ball.ycor() + ball.y_speed * ball.y_direction
    left_paddle_top_y = left_paddle.ycor() + 50
    left_paddle_bottom_y = left_paddle.ycor() - 50
    left_paddle_right_x = left_paddle.xcor() + 10
    left_paddle_left_x = left_paddle.xcor() - 10
    right_paddle_top_y = right_paddle.ycor() + 50
    right_paddle_bottom_y = right_paddle.ycor() - 50
    right_paddle_right_x = right_paddle.xcor() + 10
    right_paddle_left_x = right_paddle.xcor() - 10

    if ball.ycor() > BALL_MAX_HEIGHT or ball.ycor() < BALL_MIN_HEIGHT:
        ball.y_bounce()

    if (left_paddle_left_x <= next_ball_x <= left_paddle_right_x
            and left_paddle_top_y >= next_ball_y >= left_paddle_bottom_y):
        ball.x_bounce()
    if (right_paddle_left_x <= next_ball_x <= right_paddle_right_x
            and right_paddle_top_y >= next_ball_y >= right_paddle_bottom_y):
        ball.x_bounce()

    ball.move()



screen.exitonclick()