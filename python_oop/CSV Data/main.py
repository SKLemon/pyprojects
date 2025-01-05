# Adding information in weather_data.csv into a variable called data

"""
with open("./weather_data.csv", mode="r") as weather_data:
    data = weather_data.readlines()
"""
# The above uses the built in python library of opening and reading files. This is okay if the file is a simple text file.
# There is a better way if the file is .csv or another format where data analysis can occur... Import csv

# import csv

# temperatures = []

"""
with open("./weather_data.csv") as data_file:  # Opens the file
    data = csv.reader(data_file)  # Saves content into a variable
    next(data)  # Skips the first line in the variable (usually the header row)
    for row in data:
        temperatures.append(
            int(row[1])
        )  # Converts the second item to an integer and appends to a list
    print(temperatures)  # Prints the list

    # for row in data:
    #     if row[1] != "type":
    #       temperatures.append(int(row[1]))
    # print(temperatures)  # Prints the list
"""

""" All of the above is to open the file and extract simple numerical values from the file... Very cumbersome. Much easier to use the pandas framework """

import pandas as pd  # Importing and installing pandas library from pip is required

data_set = pd.read_csv(
    "/home/snowyp/repos/pyprojects/python_oop/CSV Data/weather_data.csv"
)

# pd.read imports the information in a file and returns a pandas dataframe. Placed into a variable for furrther processing
# data_set.head(N) Returns the first N rows of the Data Frame. Also provided a tail() method, used to show the last N rows of the Data Frame

print(data_set.head(3))  # --> Returns the first three rows
