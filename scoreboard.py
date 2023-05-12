from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setpos(0, 260)
        self.score = 0
        self.write(f"Score :  {self.score}", align="center", font=("courier", 24, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score :  {self.score}", align="center", font=("courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align="center", font=("courier", 35, "normal"))



