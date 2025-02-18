# Created as a part of the BAIL Repository... Unsure when it was originally created, but final edits completed 01/04

from question_model import Question


class QuizBrain:
    def __init__(self, question_list):
        self.q_number = 0  # Initialize question number
        self.q_list = question_list  # Store the list of questions
        self.score = 0  # Initialize score

    def still_has_questions(self):
        # Check if there are still questions left
        return self.q_number < len(self.q_list)

    # TODO: Asking the questions
    def next_question(self):
        current_question = self.q_list[
            self.q_number
        ]  # Retrieves item from question list
        user_answer = input(
            f"Q.{self.q_number + 1}: {current_question.text}. True/False: "
        )  # Prompt user for answer
        self.q_number += 1  # Increment question number
        self.check_answer(user_answer, current_question.answer)  # Check the answer

    def check_answer(self, user_answer, correct_answer):
        # Compare user answer with correct answer
        if user_answer.lower() == correct_answer.lower():
            print("You're right!")
            self.score += 1  # Increment score if correct
        else:
            print("That's wrong...")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.q_number}")
        print("\n")


# TODO: Checking if answer was correct
# TODO: Checking if we're at the end of a quiz
