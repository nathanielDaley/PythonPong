from turtle import Turtle

MAX_HEIGHT = 220
MIN_HEIGHT = -220
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, start_position):
        super().__init__()
        self.start_position = start_position
        self.direction = ""
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(self.start_position)

    def move(self):
        if self.direction == "up" and self.ycor() <= MAX_HEIGHT:
            self.setposition(self.xcor(), self.ycor() + MOVE_DISTANCE)
        if self.direction == "down" and self.ycor() >= MIN_HEIGHT:
            self.setposition(self.xcor(), self.ycor() - MOVE_DISTANCE)

    def start_up(self):
        self.direction = "up"

    def start_down(self):
        self.direction = "down"

    def stop(self):
        self.direction = ""