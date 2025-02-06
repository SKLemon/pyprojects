# Created for BAIL Repository 02/03

import smtplib, datetime, os
import dotenv
from email.message import EmailMessage

# TODO: Implement logging

# Loading the env file. Place this file in root or explicitly place the filepath
message = EmailMessage()
dotenv.load_dotenv()
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
EMAIL_APP_PSWD = os.getenv("EMAIL_APP_PSWD")

try:
    # Inilialize SMTP connection
    print("Initializing SMTP server connection...")
    server = smtplib.SMTP(host=SMTP_SERVER, port=SMTP_PORT)  # type: ignore
    server.starttls()
    print("Server auth successful.")

    # Starting user authentication
    print("Initializing user authentication...")
    server.login(user=SMTP_USERNAME, password=EMAIL_APP_PSWD)  # type: ignore
    print("User auth complete")

    # Confirming message details loop
    while True:
        message["To"] = input("Enter receiver email: ").strip()
        message["From"] = input("Enter sender email: ").strip()
        message["Subject"] = input("Enter subject: ").strip()
        message.set_content(input("Enter your message: ").strip())

        print(f"\n {message}")
        confirm = input("Press Y to send the above or N to retype: ").strip().upper()

        if confirm == "Y":
            print("Sending message")
            server.send_message(message)
            print("Message sent")
            break
        elif confirm == "N":
            print("Resetting...")
# Error catching
except Exception as e:
    print(f"Error: {e}")

# Closing the server connection once no longer in use
finally:
    server.quit()
