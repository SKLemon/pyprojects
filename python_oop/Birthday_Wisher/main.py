# Created as a part of BAIL 02/09
# ! Morality Clause for the Automated Birthday Wisher

"""
This automated birthday wisher is meant to remind you of birthdays and catch those "Oh no!" moments before they happen.
It's not here to replace human connections. A program emailing "Happy Birthday!" isn't quite the same as calling your loved one on their special day...
Additionally, who emails "Happy Birthday" messages nowadays...

If you believe birthdays should always be remembered the old-fashioned way, feel free to pick up the phone and dial away!
This program just ensures you never get hit with the "Oh no, I forgot!" panic again.
Use responsibly, and when in doubt, add a personal touch — because even a robot knows that relationships shouldn't fully automated.
"""

# TODO []: .env file set up
# TODO []: Birthdays.csv file needs creating/updated
# TODO []: Emails you a list of names to wish happy birthday

import pandas as pd
import datetime as dt
import logging as logging
from dotenv import load_dotenv

# Loads env, sets logger configs
load_dotenv(verbose=True)

logging.basicConfig(
    filename="./app.log",
    style="{",
    level="INFO",
    format="{asctime}:{levelname}::{message}",
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
        (file_data.month == today.month) & (file_data.day == today.day)
    ]
    return file_match


def birthday_info():
    """Runs main function. Outputs list of names that match today's birthdays

    Returns:
        None if empty
    """

    birthday_data = read_csv_file("./birthdays.csv")
    matching_dates = today_birthdays(birthday_data)

    if matching_dates.empty:
        logging.info("No Birthdays Today")
        return None

    else:
        matching_dates.to_csv(path_or_buf="./birthdays_list.csv")
        logging.info(
            "Birthdays found. 'birthdays_list.csv' created successfully in root"
        )


# Call the main function to output a list of today's birthdays, if any
birthday_info()
