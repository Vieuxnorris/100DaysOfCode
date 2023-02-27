from pprint import pprint
import requests

URL_SHEET = "https://api.sheety.co/cb9aae7ba107a14822530821c1301289/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=URL_SHEET)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{URL_SHEET}/{city['id']}",
                json=new_data
            )
            print(response.text)
