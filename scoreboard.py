from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("score_record.txt") as data:
            self.highscore = int(data.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-00, 270)
        self.update_score()
        self.hideturtle()

    def increase_score(self):
        """increases the score and updates the screen"""
        self.score += 1
        self.update_score()

    def check_highscore(self):
        with open("score_record.txt") as data:
            self.highscore = int(data.read())
        if self.score > self.highscore:
            with open("score_record.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.update_score()

    def reset(self):
        self.check_highscore()
        self.score = 0
        self.update_score()

    def update_score(self):
        """updates the score"""
        self.clear()
        self.write(f"Score: {self.score} \t\t\t\t\tHigh Score: {self.highscore}", False, align="center", font=('Tahoma', 15, 'normal'))

    def game_over(self):
        """stops the game"""
        self.goto(0, 240)
        self.write("GAME OVER!", False, align="center", font=('Tahoma', 15, 'normal'))
