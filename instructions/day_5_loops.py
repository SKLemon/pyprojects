#Created as a part of the BAIL repository on Github. Created 01/19/2024

# # For loops
# - Can be used in combination with lists
# - Can go through each item in a list and perform an action

# fruits = ["Apple", "Peach", "Pear"] # List of fruits, estabilished using standard list notation
# for fruit in fruits: #Assigns "fruit" to each item in the list one by one. Once the list item is printed (or whatever action the for loop is doing has finished once), it loops back and goes to the next one
#     print(fruit) # Indenting allows more actions to be placed inside a loop. Careful with indentation as all actions indented after the colon means it will loop as many times as the loop is coded for
#     print(fruit + "Pie") 

########################
# Making the average heights calculator using a list
student_heights = [180, 124, 165, 173, 189, 169, 146]
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)