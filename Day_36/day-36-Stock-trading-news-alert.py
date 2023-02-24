import os
import requests
import math
import html
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

PARAMS_STOCK = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": os.environ["STOCK_API"],
}

PARAMS_NEWS = {
    "q": COMPANY_NAME,
    "pageSize": 3,
    "apiKey": os.environ["NEWS_API"],
}


def requestStockPrice():
    with requests.get(url="https://www.alphavantage.co/query", params=PARAMS_STOCK) as stock:
        stock.raise_for_status()
        TimeSeries = stock.json()["Time Series (Daily)"]
        listDates = [value for (key, value) in TimeSeries.items()]
        stockPrice = float(listDates[0]['4. close']) - float(listDates[1]['4. close'])
        stockPriceRound = math.ceil(stockPrice / float(listDates[0]['4. close']) * 100)
        if -5 <= stockPriceRound <= 5:
            requestNewsPaper(stockPriceRound)


def requestNewsPaper(arg_stockPriceRound: int):
    with requests.get(url="https://newsapi.org/v2/everything", params=PARAMS_NEWS) as news:
        news.raise_for_status()
        newsPapers = news.json()
        headLine = html.unescape(newsPapers['articles'][0]["title"])
        brief = html.unescape(newsPapers['articles'][0]["description"])
        if arg_stockPriceRound < 0:
            titleMessage = f"{STOCK}: 🔻{abs(arg_stockPriceRound)}"
        else:
            titleMessage = f"{STOCK}: 🔺{abs(arg_stockPriceRound)}"
        sendSMS(headLine, brief, titleMessage)


def sendSMS(arg_headLine: str, arg_brief: str, arg_titleMessage: str):
    account_sid = "ACc2e766270f4c28a1294bf59a4a837eaa"
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"{arg_titleMessage}\nHeadline: {arg_headLine}\nBrief: {arg_brief}",
        from_="PHONE TWILIO",
        to="YOUR PHONE",
    )
    print(message.sid)


requestStockPrice()
