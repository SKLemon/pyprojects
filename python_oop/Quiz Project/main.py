# Created as a part of the BAIL Repository... Unsure when it was originally created, but final edits completed 01/04

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

# Create a list of Question objects from the question data
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

# Initialize the quiz with the list of questions
quiz = QuizBrain(question_bank)

# Continue asking questions until there are no more left
while quiz.still_has_questions():
    quiz.next_question()

# Print the final score after the quiz is completed
print(f"You've completed the quiz. \n Your final score is {quiz.score}/{quiz.q_number}")
