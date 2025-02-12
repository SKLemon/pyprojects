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

# TODO [✔]: .env file set up
# TODO [✔]: Birthdays.csv file needs creating/updated
# TODO [✔]: Checking if today matches a date in the birthdays.csv
# TODO []: Implement personalized Birthday with Age. Ex(Happy 23rd Birthday!)
# TODO [✔]: If today's date matches a date in the csv file, then pick a random letter from the templates
# TODO [✔]: Change any and all placeholders in the email with actual data from csv file
# TODO []: Send email
# TODO [✔]: Refactoring
# TODO []: Might change this to an email reminder, instead of an auto email sender...

import pandas as pd
import datetime as dt
import logging as logging
import smtplib, random
from email.message import EmailMessage
from dotenv import load_dotenv


# Loads env, sets logger configs
load_dotenv(verbose=True)

logging.basicConfig(
    filename="./app.log",
    style="{",
    level="INFO",
    format="{asctime}--{levelname}--{message}",
)


def read_csv_file(file_path):
    """Reads CSV file and returns the data with error handling

    Arguments:
        (str) file_path -- relative or abs file system path

    Returns:
        The data contained in the csv file
    """
    try:
        file_data = pd.read_csv(file_path)

        if file_data.empty:
            logging.warning("birthdays.csv is empty")

    except FileNotFoundError:
        logging.error("birthdays.csv not found")
        return pd.DataFrame()
    return file_data


def today_birthdays(file_data):
    """Compares todays date with any dates that match in a csv file

    Arguments:
        file_data -- Must be a Pandas DataFrame containing "month", "day", "year", "name", and "email" column headers,
            pd.read_csv()

    Returns:
        Matching dates
    """
    today = dt.datetime.today()
    file_match = file_data[
        (file_data.month == today.month) & (file_data.day == today.day)  # type: ignore
    ]
    return file_match


def replace_template(name):
    """Chooses a random template placed in /templates directory, with the file names as "template{x}.txt" where x is 1,2 or 3.

    Arguments:
        name -- values in Series "name" from the Pandas DataFrame. Used to replace the "[Name] placeholder in the message templates.

    Returns:
        Rewritten message with the name from DataFrame
    """
    num = random.randint(1, 3)
    with open(file=f"./templates/template{num}.txt", mode="r") as file:
        old_message = file.read()
        new_message = old_message.replace("[Name]", name)
    return new_message


def birthday_info():
    """birthday_info If any birthdays_summary_

    Returns:
        None, or "no birthdays today" if no dates match the Pandas DataFrame
    """

    birthday_data = read_csv_file("./birthdays.csv")
    matching_dates = today_birthdays(birthday_data)
    # current_year = dt.datetime.today().year

    if matching_dates.empty:
        return logging.info("No Birthdays Today")

    for _, row in matching_dates.iterrows():
        name = row["name"]
        # birth_year = row["year"]
        # age = current_year - birth_year
        # email = row["email"]
        birthday_message = replace_template(name)
        logging.info(birthday_message)


birthday_info()
