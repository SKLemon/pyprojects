# Created for BAIL repository on 01/07

"""
List Comprehensions...
- Unique to Python. Not alot of other programming languages have this
- Summary: Creating a new list from a previous list. We have been doing this with for loops, example below:
# To create a new list where each number is increased by 1

# numbers [1,2,3]
# new-List = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

List Comprehensions turns that 4 lines of code into 1. Looks like the below:
# new_list = [new_item for item in list]

To use the above format in making the numbers code shorter:
new_list = [n + 1 for n in numbers]
"""


""" Challenge - To create a new list from numbers, where you add 1 to each value """

# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]

# print(new_numbers)  # To check

"""
This can also work with others sequences, such as string. Shown below

name = "Angela"
new_list = [letter for letter in name] # Should just output Angela 6 times (the number of letters in Angela)
# Actually just adds each of the letters in the string into the list as individual letters...
# Output --> new_list = []"A", "n", "g", "e", "l", "a"]

These items, such as lists, string, tuple, range etc, are called sequences. This is because they have a specific order.
Performing a list comprehension takes the list and goes through the function in that order and does something to it
"""

""" Challenge: Take an iterable range (1 and 5) and create a new list where each of the numbers in the range are doubled."""

# range_list = [n * 2 for n in range(1, 5 + 1)]
# print(range_list)

"""
Conditional List Comprehensions:
Takes the standard list comprehension a little bit further.
Syntax:
new_item =[new_item for item in list if test] # Adds an if function if the test passes. Example:
"""
# names = ["alex", "bethany", "dave", "Fred", "Eleanor", "caroline"]
# new_name = [name for name in names if len(name) < 5]
### Challenge: To create a new list that contains the names longer than 5 character in ALL CAPS

# cap_name = [name.upper() for name in names if len(name) > 5]

# This shows you can have functions inside list comprehensions...

"""
##### Coding Challenge #####

Squaring Numbers
You are going to write a List Comprehension to create a new list called squared_numbers.
This new list should contain every number in the list numbers but each number should be squared.

e.g.

4 * 4 = 16

4 squared equals 16.

**DO NOT** modify the List numbers directly. Try to use List Comprehension instead of a Loop.

Target Output

[1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
"""
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num**2 for num in numbers]
# print(squared_numbers)

"""
##### Coding Challenge #####

Filtering Even Numbers
In this list comprehension exercise you will practice using list comprehension to filter out the even numbers from a series of numbers.



First, use list comprehension to convert the list_of_strings to a list of integers called numbers.

Then use list comprehension again to create a new list called result.

This new list should only contain the even numbers from the list numbers.

Again, try to use Python's List Comprehension instead of a Loop.
"""
# list_of_strings = ["9", "0", "32", "8", "2", "8", "64", "29", "42", "99"]
# numbers = [int(num) for num in list_of_strings]
# result = [even_num for even_num in numbers if even_num % 2 == 0]
# print(result)

"""
##### Coding Challenge: #####

Data Overlap

Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files.

e.g. if file1.txt contained:

1
2
3

and file2.txt contained:

2
3
4

result = [2, 3]

IMPORTANT:  The output should be a list of integers and not strings!

Try to use List Comprehension instead of a Loop.
"""

with open("./file1.txt", mode="r") as files:
    file1_data = [int(x.strip()) for x in files]

with open("./file2.txt", mode="r") as files2:
    file2_data = [int(x.strip()) for x in files2]

# result = [
#     each_item
#     for each_num in file1_data
#     for each_item in file2_data
#     if each_num == each_item
# ]
# print(result)

# The solution above is what I wrote...and based on the instructions it is not incorrect.
# It returns pairwise matches, which essentially compares every item in one list against every item in another list.
# If they match, it returns them.
# This is why the extra "3" was being returned, as it matches the "3" twice.
# Once at the beginning, then again at line 8 in file 2.
# This is also known as nested comprehension

# The below code is correct as well, as it only returns if there is a match at least once. It does not take into account multiple matches
result = [int(num) for num in file1_data if num in file2_data]

# Both work depending on context but both will work for their own suitable applications... Good to know both I guess
print(result)
