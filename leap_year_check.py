#Created as a part of the BAIL repository on Github. Created 01/14/2024

#Getting input from user to check if a year is a leap year or not
year = int(input("Type in a year to check if it is a leap year or not\n"))

# The rules are:
# If a year is divisible by 4 it is a leap year
# If it is not divisible by 100 it is a leap year
# UNLESS it is also divisible by 400, in which case it is a leap year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
  print("Leap year")
else:
  print("Not leap year")