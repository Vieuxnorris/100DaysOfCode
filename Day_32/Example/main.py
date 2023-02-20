import smtplib

# MY_EMAIL = "address mail"
# MY_PASSWORD = "Key application google gmail"
#
# with smtplib.SMTP("smtp.gmail.com") as gmail:
#     gmail.starttls()
#     gmail.login(user=MY_EMAIL, password=MY_PASSWORD)
#     gmail.sendmail(from_addr=MY_EMAIL,
#                    to_addrs="mail",
#                    msg="Subject:Hello\n\nThis is the body of my email")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1997, month=6, day=6)
print(date_of_birth)
