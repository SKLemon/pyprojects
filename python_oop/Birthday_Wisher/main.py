# Created as a part of BAIL 02/09
# ! Morality Clause for the Automated Birthday Wisher

"""
This automated birthday wisher is meant to remind you of birthdays and catch those "Oh no!" moments before they happen.
It's not here to replace human connections and a program emailing "Happy Birthday!" isn't quite the same as calling your loved one...
Additionally, who emails "Happy Birthday" messages nowadays...

If you believe birthdays should always be remembered the old-fashioned way, feel free to pick up the phone and dial away!
This program just ensures you never get hit with the "Oh no, I forgot!" panic again.
Use responsibly, and when in doubt, add a personal touch — because even a robot knows that friendships shouldn't be fully automated.
"""

# TODO []: .env file set up
# TODO [✔]: Birthdays.csv file needs creating/updated
# TODO [✔]: Checking if today matches a date in the birthdays.csv
# TODO []: Implement personalized Birthday with Age. Ex(Happy 23rd Birthday!)
# TODO []: If today's date matches a date in the csv file, then pick a random letter from the templates
# TODO []: Change any and all placeholders in the email with actual data from csv file
# TODO []: Send email
# TODO []:


import pandas as pd
import datetime as dt
import logging as logging
import os, smtplib, random
from email.message import EmailMessage
from dotenv import load_dotenv

# Loads env, sets logger configs, the birthday file, and gets today's date
load_dotenv(dotenv_path="./.env", verbose=True)
logging.basicConfig(filename="./app.log", style="{", level="INFO")
today = dt.datetime.today()
birthday_data = pd.read_csv("./birthdays.csv")


def birthday_info(today, birthdays):
    # Checking for matches
    matching = birthdays[
        (birthdays.month == today.month) & (birthdays.day == today.day)
    ]

    if matching.empty:
        logging.info("no birthdays today")
    else:
        for _, row in matching.iterrows():
            name = row["name"]
            birth_year = row["year"]
            age = today.year - birth_year
            return name, birth_year, age

    # Reads the files and places them into a list for selection
    # Since the template files are in a "template{num}" format, with num being 1,2 or 3

    num = random.randint(1, 3)
    with open(file=f"./templates/template{num}.txt", mode="r") as file:
        message = file.read()

    print(message)


birthday_info(today, birthday_data)
