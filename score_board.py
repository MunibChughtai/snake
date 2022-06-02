from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.setposition(0,275)
        self.score=0
        self.write(f"Score: {self.score}", align = "center", font=('Arial', 18, 'bold'))
    
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align = "center", font=('Arial', 18, 'bold'))

    def game_over(self):
        # self.clear()
        self.setposition(0,0)
        self.write(f"GAME OVER", align = "center", font=('Arial', 18, 'bold'))