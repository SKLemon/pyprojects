# Created as a part of BAIL repository on 01/04

"""
Objective is to:

TODO[✔]: Create a csv called squirrel count
TODO[✔]: Squirrel count must have a small table, containing fur colour and count

"""
#####

import pandas as pd

# Uncomment the below import to generate the barchart
# import matplotlib.pyplot as plt

data_set = pd.read_csv(
    "/home/snowyp/repos/pyprojects/python_oop/Squirrel Census/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
)

# The below identifies which unique colors are in the data set
squirrel_data = data_set["Primary Fur Color"].drop_duplicates()

squirrel_dict = {}

# Slicing the list ensures useless values (like nan) are excluded
squirrel_dict["Fur Colour"] = squirrel_data[1:]

gray_count = len(data_set[data_set["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data_set[data_set["Primary Fur Color"] == "Cinnamon"])
black_count = len(data_set[data_set["Primary Fur Color"] == "Black"])

squirrel_dict["Count"] = gray_count, cinnamon_count, black_count

pd.DataFrame(squirrel_dict).to_csv(
    "/home/snowyp/repos/pyprojects/python_oop/Squirrel Census/squirrel_count.csv"
)

""" Uncomment the below to generate a bar chart. Must have matplotlib installed """
# df = pd.DataFrame(squirrel_dict)
# df.plot(x="Fur Colour", y="Count", kind="bar", legend=False)
# plt.title("Squirrel Fur Color Count")
# plt.ylabel("Count")
# plt.show()
