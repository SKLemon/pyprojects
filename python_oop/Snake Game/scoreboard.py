from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 32, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 240)

    def increase_score(self):
        """Increase the score by 1, clear the previous score, and write the new score."""
        self.score += 1
        self.clear()
        self.write(
            f"Score: {self.score}",
            align=ALIGN,
            font=FONT,
        )

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(
            f"Game Over. Final Score: {self.score}",
            align=ALIGN,
            font=FONT,
        )
