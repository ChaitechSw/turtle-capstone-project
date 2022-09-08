
from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=1
        self.color("black")
        self.penup()
        self.goto(x=-280,y=260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level:{self.score}",align='left', font=FONT)

    def game_over(self):
        self.goto(x=0,y=0)
        self.write(f"GAME OVER", align='center',font=('Arial', 18, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()