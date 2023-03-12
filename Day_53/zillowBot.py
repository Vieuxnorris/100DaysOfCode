import requests
import re

from utils import HEADERS
from bs4 import BeautifulSoup


class ZyllowBot:
    def __init__(self):
        self.links = []
        self.prices = []
        self.address = []
        self.urlZyllow = None

    def research(self, city: str):
        """
        city -> all input str
        """
        if bool(city):
            self.urlZyllow = f"https://www.zillow.com/{city}/for_rent/" \
                             "?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22" \
                             "west%22%3A-122.63417331103516%2C%22east%22%3A-122.23248568896484%2C%22south%22%" \
                             "3A37.66584942288767%2C%22" \
                             "north%22%3A37.884572713401546%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3" \
                             "Atrue%2C%22" \
                             "filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A100000%7D%2C%22mp%22%3A%7B%" \
                             "22min%22%3A510%7D%2C%22" \
                             "fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22" \
                             "fsbo%22%3A%7B%22value%22%" \
                             "3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%" \
                             "3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3" \
                             "Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
        else:
            self.urlZyllow = f"https://www.zillow.com/home/for_rent/" \
                             "?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22" \
                             "west%22%3A-122.63417331103516%2C%22east%22%3A-122.23248568896484%2C%22south%22%" \
                             "3A37.66584942288767%2C%22" \
                             "north%22%3A37.884572713401546%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3" \
                             "Atrue%2C%22" \
                             "filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A100000%7D%2C%22mp%22%3A%7B%" \
                             "22min%22%3A510%7D%2C%22" \
                             "fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22" \
                             "fsbo%22%3A%7B%22value%22%" \
                             "3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%" \
                             "3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3" \
                             "Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

    def processSoup(self):
        try:
            with requests.get(url=self.urlZyllow, headers=HEADERS) as htmlScraping:
                htmlScraping.raise_for_status()
                htmlSite = htmlScraping.text
        except requests.exceptions.HTTPError:
            print("HTTP ERROR")
        else:
            # use for test
            # with open("tempSite.html", "w", encoding="utf-8") as tempSite:
            #     tempSite.write(htmlSite)
            soup = BeautifulSoup(htmlSite, "html.parser")
            gridSearch = soup.select(selector=".jhnswL.with_constellation")
            for article in gridSearch:
                try:
                    price = article.select(".bqsBln")[0].contents[0].getText()
                    priceNorm = re.split(r'[+/]', price)
                    address = article.select(".gdfTyO address")[0].contents[0].getText()
                    link = article.select(".property-card-link")[0].get("href")
                except IndexError:
                    print("Error")
                else:
                    self.links.append(link)
                    self.address.append(address)
                    self.prices.append(priceNorm)