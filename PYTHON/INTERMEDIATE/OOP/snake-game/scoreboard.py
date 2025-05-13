from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.goto(0, 270)
        self.write(f"Score: {self.score}",True, align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",True, align=ALIGNMENT,font=FONT)

    def total_score(self):
        self.score += 1
        self.clear()
        self.update_score()

