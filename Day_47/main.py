import os
import bs4
import requests
import smtplib
from bs4 import BeautifulSoup

URL = "https://www.amazon.com.be/ASUS-GeForce-graphique-DisplayPort-TUF-RTX4090-O24G-GAMING/dp/B0BHD9TS9Q/ref=sr_1_1?crid=2XZA7YESRNEIO&keywords=rtx+4090&qid=1678109022&sprefix=rtx+4090%2Caps%2C72&sr=8-1"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Langage": "be"
}

try:
    with requests.get(url=URL, headers=HEADERS) as htmlScraping:
        htmlScraping.raise_for_status()
        htmlSite = htmlScraping.text
except requests.exceptions.HTTPError:
    print("HTTP ERROR")
else:
    try:
        soup = BeautifulSoup(htmlSite, "lxml")
    except bs4.FeatureNotFound:
        print("Couldn't find a tree builder with the features you requested: html-parser")
    else:
        prices = soup.find(name="span", class_="a-offscreen")
        price = int(prices.getText().split(",")[0].replace("\u202f", ""))
        if price <= 2000:
            message = "RTX 4090 ASUS TUF Gaming 24 Go"
            with smtplib.SMTP("smtp.gmail.com") as gmail:
                gmail.starttls()
                gmail.login(user=os.getenv("MY_EMAIL"), password=os.getenv("MY_PASSWORD"))
                gmail.sendmail(from_addr=os.getenv("MY_EMAIL"),
                               to_addrs=os.getenv("MY_PRIMARY_EMAIL"),
                               msg=f"Subject: Lower price Amazon alert\n\n{message}"
                                   f" - {str(price)}\n link: {URL}".encode("utf-8"))
