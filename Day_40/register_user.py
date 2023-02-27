import requests
import smtplib

URL_SHEET = "https://api.sheety.co/cb9aae7ba107a14822530821c1301289/flightDeals/user"


class RegisterUser:
    def __init__(self):
        self.userData = None
        self.firstName = None
        self.lastName = None
        self.email = None
        self.verifEmail = None

    def registerUser(self):
        self.userData = None
        print("Welcome to Vieuxnorris Flight Club.\n"
              "We find the best flight deals and email you.\n")
        try:
            self.firstName = input("What is your first name ? \n")
            self.lastName = input("What is your last name ? \n")
            self.email = input("What is your email ? \n")
            self.verifEmail = input("Type your email again.\n")
            if not self.firstName or not self.lastName or not self.email or not self.verifEmail:
                raise ValueError("empty string")
        except ValueError as e:
            print(e)
        else:
            if self.email.lower() == self.verifEmail.lower():
                with requests.get(url=URL_SHEET) as userGet:
                    userGet.raise_for_status()
                    numberUser = len(userGet.json()["user"][0])

                jsonUser = {
                    "user": {
                        "firstName": self.firstName,
                        "lastName": self.lastName,
                        "email": self.email,
                    }
                }
                with requests.put(url=f"{URL_SHEET}/{numberUser + 1}", json=jsonUser) as userPut:
                    userPut.raise_for_status()

    def getUserData(self):
        with requests.get(url=URL_SHEET) as userGet:
            userGet.raise_for_status()
            self.userData = userGet.json()
        return self.userData["user"]
