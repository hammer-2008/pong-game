from turtle import Turtle



class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            self.score,
            align="center",
            font=("Courier", 50, "normal")
        )

    def increase_score(self):
        self.score += 1
        self.update_score()
