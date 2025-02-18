# Created for BAIL repository on 01/12
"""
##### Dictionary Comprehension #####
- Allows to create a new dict based on the values in a list or an old dictionary
Syntax:

Dictionary Comprehension using a previous list:
I.E Creating a dictionary (key,value pair) for each item in a list
# new_dict = {new_key:new_value for item in list}

Dictionary Comprehension using a previous dictionary:
I.E Creating a new dictionary based on the values in an existing dictionary using key,value pairs
# new_dict = {new_key:new_value for (key,value) for dict.items()}

Conditional can apply at the very end (if test)
"""
### Challenge: Generate a random score for each of the students
import random

names = [
    "Alex",
    "Beth",
    "Caroline",
    "Dave",
    "Eleanor",
    "Freddie",
]
student_scores = {student: random.randint(1, 100) for student in names}

print(student_scores)

### Challenge: Create a dictionary where students with a score greater than 60 have passed

passed_students = {
    student: score for (student, score) in student_scores.items() if score >= 60
}
print(passed_students)

"""
##### Coding Challenge #####

You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.
Try Googling to find out how to convert a sentence into a list of words.
*Do NOT** Create a dictionary directly.
Try to use Dictionary Comprehension instead of a Loop.

To keep this exercise simple, count any punctuation following a word with no whitespace as part of the word. Note that "Swallow?" therefore has a length of 8.
"""
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_list = sentence.split()
result = {word: len(word) for word in sentence_list}
print(result)

"""
Dictionary Comprehension 2
You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
To convert temp_c into temp_f use this formula:

(temp_c * 9/5) + 32 = temp_f

**Do NOT** Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
"""
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {
    day: (temperature * 9 / 5) + 32 for (day, temperature) in weather_c.items()
}

print(weather_f)

"""
This can also be applied to panda dataframes. This lesson is using loops with dataframes and iterating over them
"""

student_dict = {
    "student": [
        "Angela",
        "James",
        "Lily",
    ],
    "score": [56, 76, 98],
}

import pandas as pd

# Creating the DatFrame
student_dataframe = pd.DataFrame(student_dict)
print(student_dataframe)
#  This can also be created in several different ways
# Loop through a dataframe is possible using the same syntax as regular ol Python, using the below.

# for key, value in student_dataframe.items():
#     print(value)

# Pandas has a built in loop called itterows and can be used to make your life simpler
for index, row in student_dataframe.iterrows():
    print(
        row.score
    )  # Will print only the scores. print(row.student) will print the student names only
