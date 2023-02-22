import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

ACCOUNT_SID = "account twilio id here"
AUTH_TOKEN = "your twilio token here"

params = {
    "lat": 0,
    "lon": 0,
    "exclude": "current,daily,minutely,alerts",
    "appid": "appid openweather",
}

hourlyWeather = []

def requestWeather():
    with requests.get("https://api.openweathermap.org/data/3.0/onecall?", params=params) as weather:
        weather.raise_for_status()
        data = weather.json()
        for hourly in data["hourly"][:12]:
            if int(hourly["weather"][0]["id"]) < 600:
                proxyClient = TwilioHttpClient()
                proxyClient.session.proxies = {'https': os.environ['https_proxy']}
                client = Client(ACCOUNT_SID, AUTH_TOKEN, http_client=proxyClient)
                message = client.messages.create(
                    body="It's going to rain today. Remember to bring an ☂️",
                    from_="phone number twilio",
                    to="your phone number"
                )
                print(message.status)
                break

requestWeather()
