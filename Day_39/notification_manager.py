import os

from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def sendSMS(self, dataGoogleSheet, flightInfos):
        if dataGoogleSheet['lowestPrice'] >= flightInfos.price:
            account_sid = "ACc2e766270f4c28a1294bf59a4a837eaa"
            auth_token = os.environ["TWILIO_TOKEN"]
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=f"Low price alert! Only €{flightInfos.price} to fly from {flightInfos.origin_city}"
                     f"to {flightInfos.destination_city}, from {flightInfos.out_date} to {flightInfos.return_date}.",
                from_="+12706336456",
<<<<<<< HEAD
                to=os.getenv("PHONE_NUMBER")
=======
                to=Your Phone Number
>>>>>>> 5a1e3ad1dfb9e297de6e6bf01cf5ed43354f5ed7
            )
            print(message.sid)
