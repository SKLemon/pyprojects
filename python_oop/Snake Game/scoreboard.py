from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 32, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0  # Initialize score to 0
        self.highscore = 0
        self.hideturtle()  # Hide the turtle cursor
        self.color("white")  # Set the color to white
        self.penup()  # Lift the pen to avoid drawing lines
        self.goto(0, 240)  # Position the scoreboard at the top center
        self.update_scoreboard()

    def increase_score(self):
        """Increase the score by 1, clear the previous score, and write the new score."""
        self.score += 1  # Increment the score
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT
        )

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     """Display the game over message with the final score."""
    #     self.goto(0, 0)  # Move to the center of the screen
    #     self.clear()  # Clear the previous score
    #     self.write(
    #         f"Game Over. Final Score: {self.score}",
    #         align=ALIGN,
    #         font=FONT,
    #     )  # Display the game over message
