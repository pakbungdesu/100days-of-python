import smtplib
from smtplib import SMTPException
import requests
import datetime as dt


# -------------------- CONSTANT ------------------- #
MY_LAT = 34.0479  # you can custom latitude and longitude here
MY_LONG = -168.0621
MY_EMAIL = "example1@gmail.com"
MY_PASSWORD = "insert_app_password_here"
TO_EMAIL = "example2@gmail.com"


# --------------------- FUNCTION --------------------- #
def send_email(from_email, password, to_email, some_txt):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as connection:
            connection.starttls()  # TLS encryption
            connection.login(from_email, password)  # App password for 2FA
            connection.sendmail(from_email, to_email, some_txt)
            print("Email sent successfully!")
            return True
    except TimeoutError:
        print("Connection timed out. Please check your network connectivity.")
    except SMTPException as e:
        print(f"Error sending email: {e}")  # Print specific error message


# ------------------------- REQUEST ------------------------ #
success = False
while not success:
    res = requests.get("http://api.open-notify.org/iss-now.json")

    if res.status_code == requests.codes.ok:
        data = res.json()
        curr_lat = float(data["iss_position"]["latitude"])
        curr_long = float(data["iss_position"]["longitude"])

        if MY_LAT - 5 <= curr_lat <= MY_LAT + 5 and MY_LONG - 5 <= curr_long <= MY_LONG + 5:
            timestamp = data["timestamp"]
            dt_object = dt.datetime.fromtimestamp(timestamp)

            with open("my_letter.txt", "r") as readfile:
                content = readfile.read()
                content = content.replace("[datetime]", f"{dt_object}")
                content = content.replace("[latitude]", f"{curr_lat}")
                content = content.replace("[longitude]", f"{curr_long}")
                message = f"Subject: A lovely message from myself!\n\n{content}\n"
                success = send_email(MY_EMAIL, MY_PASSWORD, TO_EMAIL, message)

    else:
        print("Error:", res.status_code, res.text)
