from turtle import Turtle

TEXT_ALIGN = "center"
TEXT_FONT = ("Courier", 80, "normal")
SCOREBOARD_HEIGHT = 200
LEFT_SCORE_X_POSITION = -100
RIGHT_SCORE_X_POSITION = 100

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.draw_score()

    def draw_score(self):
        self.goto(LEFT_SCORE_X_POSITION, SCOREBOARD_HEIGHT)
        self.write(self.left_score, align=TEXT_ALIGN, font=TEXT_FONT)
        self.goto(RIGHT_SCORE_X_POSITION, SCOREBOARD_HEIGHT)
        self.write(self.right_score, align=TEXT_ALIGN, font=TEXT_FONT)

    def increase_left_score(self):
        self.left_score += 1
        self.clear()
        self.draw_score()

    def increase_right_score(self):
        self.right_score += 1
        self.clear()
        self.draw_score()