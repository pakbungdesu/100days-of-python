"""
ISS Overhead Notifier
Automatically tracks the International Space Station (ISS) via API.
If the ISS is within +5/-5 degrees of the user's location, it sends a
customized notification email using SMTP.
"""

import smtplib
from smtplib import SMTPException
import requests
import datetime as dt
import time

# -------------------- CONSTANTS ------------------- #
# Your current GPS coordinates
MY_LAT = 15.870032
MY_LONG = 100.992541

# Email Credentials
MY_EMAIL = "example1@gmail.com"
# Note: This should be a 16-character App Password, not your regular login password.
MY_PASSWORD = "insert_app_password_here"
TO_EMAIL = "example2@gmail.com"


# --------------------- FUNCTIONS --------------------- #

def send_email(from_email, password, to_email, some_txt):
    """
    Establishes a secure connection to the Gmail SMTP server and sends an email.

    Args:
        from_email (str): The sender's email address.
        password (str): The Google App Password.
        to_email (str): The recipient's email address.
        some_txt (str): The formatted message including Subject line.

    Returns:
        bool: True if sent successfully, False otherwise.
    """
    try:
        # Connect to Gmail's SMTP server on port 587 (Standard for TLS)
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as connection:
            connection.starttls()  # Upgrade the connection to secure TLS encryption
            connection.login(from_email, password)
            connection.sendmail(from_email, to_email, some_txt)
            print("Email sent successfully!")
            return True
    except TimeoutError:
        print("Connection timed out. Check your network.")
        return False
    except SMTPException as e:
        print(f"SMTP Error: {e}")
        return False


# ------------------------- MAIN LOGIC ------------------------ #

success = False
# The loop continues until the ISS is in range and the email is successfully sent
while not success:
    # Request real-time ISS position from Open Notify API
    res = requests.get("http://api.open-notify.org/iss-now.json")

    # Check if the HTTP request was successful (Status Code 200)
    if res.status_code == requests.codes.ok:
        data = res.json()
        curr_lat = float(data["iss_position"]["latitude"])
        curr_long = float(data["iss_position"]["longitude"])

        # Check if the ISS is within a +/- 5 degree margin of your position
        if MY_LAT - 5 <= curr_lat <= MY_LAT + 5 and MY_LONG - 5 <= curr_long <= MY_LONG + 5:
            timestamp = data["timestamp"]
            dt_object = dt.datetime.fromtimestamp(timestamp)

            # --- Letter Personalization ---
            try:
                with open("my_letter.txt", "r") as readfile:
                    content = readfile.read()
                    # Replace placeholders with real-time data
                    content = content.replace("[datetime]", f"{dt_object}")
                    content = content.replace("[latitude]", f"{curr_lat}")
                    content = content.replace("[longitude]", f"{curr_long}")

                    # Construct email with Subject line (essential for Gmail)
                    message = f"Subject: ISS is Overhead! 🛰️\n\n{content}\n"
                    success = send_email(MY_EMAIL, MY_PASSWORD, TO_EMAIL, message)
            except FileNotFoundError:
                print("Error: my_letter.txt not found. Please create the template file.")
                break

    else:
        print(f"API Error: {res.status_code}")
        time.sleep(60)
