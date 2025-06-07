from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.create_left()
        self.create_right()
        self.create_middle()

    def create_left(self):
        self.goto(-150, 260)
        self.write(
            f"Score: {self.l_score}",
            align=ALIGN,
            font=FONT,
        )

    def create_right(self):
        self.goto(150, 260)
        self.write(
            f"Score: {self.r_score}",
            align=ALIGN,
            font=FONT,
        )

    def create_middle(self):
        self.goto(0.00, 300.00)
        self.seth(270)
        while self.ycor() > -300.00:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

    def update_left(self):

        self.l_score += 1
        self.clear()
        self.create_left()
        self.create_right()
        self.create_middle()

    def update_right(self):

        self.r_score += 1
        self.clear()
        self.create_left()
        self.create_right()
        self.create_middle()
