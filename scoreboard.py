from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.add_score()

    def level_up(self):
        self.clear()
        self.level += 1
        self.add_score()

    def add_score(self):
        self.write(f"Level: {self.level}", False, "left", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)
