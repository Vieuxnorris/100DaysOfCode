import requests
import datetime as dt
import smtplib
import time

MY_EMAIL = "mail"
MY_PASSWORD = "key api"

MY_LAT = 1
MY_LNG = 1
TIME_NOW = dt.datetime.now()

parametersSunrise = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}


def sendMail():
    with requests.get(url="http://api.open-notify.org/iss-now.json") as reponse:
        reponse.raise_for_status()
        data = reponse.json()
        issPosition = (data['iss_position']['latitude'], data['iss_position']['longitude'])

    with requests.get(url="https://api.sunrise-sunset.org/json", params=parametersSunrise) as reponse:
        reponse.raise_for_status()
        data = reponse.json()
        sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
        sunset = data['results']['sunset'].split("T")[1].split(":")[0]

    if MY_LAT - 5 <= float(issPosition[0]) <= MY_LAT + 5 and MY_LNG - 5 <= float(issPosition[1]) <= MY_LNG + 5:
        if TIME_NOW.hour >= int(sunset) or TIME_NOW.hour <= int(sunrise):
            with smtplib.SMTP("smtp.gmail.com") as gmail:
                gmail.starttls()
                gmail.login(user=MY_EMAIL, password=MY_PASSWORD)
                gmail.sendmail(from_addr=MY_EMAIL,
                               to_addrs="mail",
                               msg=f"Subject:ISS look the sky bro!\n\nThe ISS is above you in the sky.")


while True:
    time.sleep(60)
    print("Scan ISS")
    sendMail()
