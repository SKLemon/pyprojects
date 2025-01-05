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
    "/home/snowyp/repos/pyprojects/python_oop/Instructions/Pandas Module/CSV Data/weather_data.csv"
)

# pd.read imports the information in a file and returns a pandas DataFrame. Placed into a variable here for further processing.
# data_set.head(N) Returns the first N rows of the Data Frame. Also provided a tail() method, used to show the last N rows of the Data Frame.

# print(data_set.head(3))  # --> Returns the first three rows

# DataFrame is equivalent to a table in excel, and Series is equivalent to a list.
# Can convert DataFrame objects to different pythonic data sets (dictionary, Series into lists, etc)

# Uncomment the below to convert the DataFrame object into a dictionary and place it into a variable
# data_dict = (data_set.to_dict())

# Uncomment the below to convert the "temperature" Series into a list and place it into a variable
# temp_list = data_set["temp"].to_list()

""" Challenge is to get the average of all the temperatures in the weather data """

# average = round(sum(temp_list) / len(temp_list), 2)
# print(f"The average is: {average}")  # This will print 17.43

""" The above is using standard math and python code. Pandas has a built in method to get the mean of the Series. Ex. shown below:
Important thing to note here is to take the series directly from the pd.read() rather than taking the converted variable on line 50 """

print(f"The average using Series methods is: {round(data_set['temp'].mean(),2)}")

""" Challenge is to get the maximum value using the Series methods. """

print(f"The max value using the Series method is: {data_set['temp'].max()}")

# Getting data from columns...

"""
When working with pandas its easy to get data from columns just by using the label of the first row "temperature", "condition" as an argument when calling the data set etc
Above, we used square bracket notation to identify the Series... We can also just call the attribute matching the label of the column itself... Example: data_set.temperature
Pandas converts the header rows into attributes automatically. These are type sensitive...
data_set.Temperature (note the capital "T") will not work, as there is no column with the Temperature (capital T) label.
 """
# Getting data from an individual row

"""
Pulling information from individual rows is done by using calling the data set, then getting information from the column where the row is equal to whatever you want it to be equal to. Example:
data_set --> Identifies the dataset
[data_set.day] --> Calls the column (note the .day attribute)
== "Monday" -- > identifies the row we need that matches our requirement.

"""
data_set[data_set.day == "Monday"]  # Will result in: 0  Monday    12     Sunny

""" Challenge is to get the row of data where temperature was at its highest """

## Find highest temperature Series
high_temp = data_set.temp.max()
print(data_set[data_set.temp == high_temp])

""" Also possible to convert indivdual rows (and the information they contain) into a variable for further processing. The below allows to use the variable 'monday' and call the columns that are associated (condition, temperature etc)"""

monday = data_set[data_set.day == "Monday"]
# print(monday.condition)  # Will print 0  Sunny, as Monday's condition is Sunny

""" Challenge is to convert Monday's temperature into Fahrenheight """

# print(monday.temp[0])

# fahrenheight = monday.temp[0] * (9 / 5) + 32

# print(fahrenheight)

# Create a DataFrame from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}
data_table = pd.DataFrame(data_dict)
# Converts the dictionary above into a DataFrame usable by pandas

# Can save the file and output to .csv format. Needs path location
data_table.to_csv(
    "/home/snowyp/repos/pyprojects/python_oop/Instructions/Pandas Module/CSV Data/new_csv.csv"
)
