import requests

parameters = {
    "amount": 50,
    "type": "boolean",
}


class Data:
    def __init__(self):
        self.questionData = {}

    def getQuestions(self):
        with requests.get(url="https://opentdb.com/api.php", params=parameters) as response:
            response.raise_for_status()
            data = response.json()
            self.questionData = data["results"]
        return self.questionData
