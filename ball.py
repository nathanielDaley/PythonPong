from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_speed = 10
        self.y_speed = 10
        self.x_direction = 1
        self.y_direction = 1
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setposition((0, 0))

    def move(self):
        self.setposition(self.xcor() + self.x_speed * self.x_direction, self.ycor() + self.y_speed * self.y_direction)

    def y_bounce(self):
        self.y_direction *= -1

    def x_bounce(self):
        self.x_direction *= -1