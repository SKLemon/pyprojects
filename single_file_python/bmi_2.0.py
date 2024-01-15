#Created as a part of the BAIL repository on Github. Created 01/24/2024

#Ask user for their height and weight - Input always converts to str so reconvert to proper data types
height = float(input("Enter your height in meters, e.g, 1.55: "))
weight = int(input("Enter your weight in kilograms e.g, 72: "))

bmi = float(weight / height ** 2) # Find BMI based on simple calc of BMI = weight divided by height squared
#Checks where the BMI number inputted above stands after calculation and prints out accordingly
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <= 25:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <= 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")
