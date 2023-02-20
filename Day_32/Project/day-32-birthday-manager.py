import smtplib
import datetime as dt
import pandas as pd
import random

MY_EMAIL = "address mail"
MY_PASSWORD = "Key application google gmail"
NOW = dt.datetime.now()
TODAY_TUPLE = (NOW.month, NOW.day)


def normalisationCsv():
    try:
        birthdayData = pd.read_csv("birthday.csv")
    except pd.errors.EmptyDataError:
        pass
    else:
        return birthdayData


def normalisationBirthday():
    birthdayData = normalisationCsv()
    birthdayDict = {(dataRow["month"], dataRow["day"]): dataRow for (index, dataRow) in birthdayData.iterrows()}
    return birthdayDict


def sendEmail():
    birthdayData = normalisationBirthday()
    if TODAY_TUPLE in birthdayData:
        birthdayInfos = birthdayData[TODAY_TUPLE]
        letter = ""
        with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt", "r") as file:
            letter = [words.replace("[NAME]", f"{birthdayInfos['name']}") for words in file.readlines()]
        with smtplib.SMTP("smtp.gmail.com") as gmail:
            gmail.starttls()
            gmail.login(user=MY_EMAIL, password=MY_PASSWORD)
            gmail.sendmail(from_addr=MY_EMAIL,
                           to_addrs=f"{birthdayInfos['email']}",
                           msg=f"Subject:Happy Birthday!\n\n{''.join(word for word in letter)}\n")


sendEmail()
