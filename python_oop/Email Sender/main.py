# Created for BAIL Repository 02/03

import smtplib, datetime as dt
import dotenv, os
import logging as logging
from email.message import EmailMessage
from pathlib import Path
import random

# TODO: Path Module
# TODO: Open file and read from it
# TODO: Randomly select a line from "./quotes.txt"
# TODO: Configure date/time to send the quote ranndomized

now = dt.datetime.today()
weekday = now.weekday()

# Only run if weekday is equal to a certain day
if weekday == 6:

    # * Setting default log configs
    # OS-agnostic - This will create a log file "app.log" in the same folder this is ran
    log_path = Path("./app.log")
    logging.basicConfig(
        filename=f"{log_path}",
        encoding="utf-8",
        datefmt="%m-%d %H:%M",
        style="{",
        level=logging.INFO,
        format="{asctime}--{levelname}:{message}",
    )

    # * Loading the env file. Create a .env and place this file in root directory
    # * Only here to secure sensitive date - NEVER HARDCODE PERSONAL DATA INTO FILES THAT ARE SHARED/UPLOADED
    dotenv.load_dotenv()  # type: ignore
    SMTP_SERVER = os.getenv("SMTP_SERVER")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    SMTP_USERNAME = os.getenv("SMTP_USERNAME")
    EMAIL_APP_PSWD = os.getenv("EMAIL_APP_PSWD")
    logging.info("Server information loaded")

    try:
        # Inilialize SMTP connection
        logging.info("Initializing SMTP server connection...")
        server = smtplib.SMTP(host=SMTP_SERVER, port=SMTP_PORT)  # type: ignore
        server.starttls()
        logging.info("Server auth successful.")

        # Starting user authentication
        logging.info("Initializing user authentication...")
        server.login(user=SMTP_USERNAME, password=EMAIL_APP_PSWD)  # type: ignore
        logging.info("User auth complete")

        # Opens the file, default read-only, to place contents into a list
        with open(file=Path("./quotes.txt")) as quote_file:
            quotes = [line.strip() for line in quote_file]

        # Prepares the message to be sent
        message = EmailMessage()
        message["To"] = SMTP_USERNAME
        message["From"] = SMTP_USERNAME
        message["Subject"] = "Your weekly positivity quote!"
        message.set_content(random.choice(quotes))
        # server.send_message(message)
        print(message)

    # Error catching
    except Exception as e:
        logging.warning(f"Error: {e}")

    # Closing the server connection once no longer in use
    finally:
        logging.info("Closing server connection...")
        server.quit()
        logging.info("Server is now closed")
