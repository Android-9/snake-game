from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreboard = 0
        with open('data.txt') as score:
            saved_score = score.read()
        self.high_score = int(saved_score)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.sety(270)
        self.write(f"Score: {self.scoreboard} High Score: {self.high_score}", align='center', font=('Impact', 20, 'normal'))

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.scoreboard} High Score: {self.high_score}", align="center", font=('Impact', 20, 'normal'))

    def game_reset(self):
        if self.scoreboard > self.high_score:
            self.high_score = self.scoreboard
            with open('data.txt', 'w') as score:
                score.write(f"{self.high_score}")

        self.scoreboard = 0
        self.update_score()

    def increase_score(self):
        self.scoreboard += 1
        self.update_score()

    # def game_over(self):
    #     self.hideturtle()
    #     self.setposition(0, 0)
    #     self.color("red")
    #     self.write("GAME OVER", align='center', font=('Impact', 28, 'normal'))



