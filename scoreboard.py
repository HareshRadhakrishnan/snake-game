from turtle import Turtle

class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(y=270, x=0)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=("Century Gothic", 16, "bold"))
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.show_score()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"game over", move=False, align="center", font=("Century Gothic", 20, "bold"))
    def refresh_score(self):
        self.score += 1
        self.clear()
        self.show_score()