import os
import smtplib

from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def sendMail(self, dataGoogleSheet, flightInfos, emails):
        if dataGoogleSheet['lowestPrice'] >= flightInfos.price:
            message = f"Low price alert! Only €{flightInfos.price} to fly from {flightInfos.origin_city}" \
                      f"to {flightInfos.destination_city}, from {flightInfos.out_date} to {flightInfos.return_date}."
            if flightInfos.stop_overs > 0:
                message += f"\nFlight has {flightInfos.stop_overs} stop over, via {flightInfos.via_city}."
            else:
                link = f"https://www.google.co.uk/flights?hl=en#flt={flightInfos.origin_airport}." \
                       f"{flightInfos.destination_airport}.{flightInfos.out_date}*{flightInfos.destination_airport}." \
                       f"{flightInfos.origin_airport}.{flightInfos.return_date}"
                with smtplib.SMTP("smtp.gmail.com") as gmail:
                    gmail.starttls()
                    gmail.login(user=os.getenv("MY_EMAIL"), password=os.getenv("MY_PASSWORD"))
                    gmail.sendmail(from_addr=os.getenv("MY_EMAIL"),
                                   to_addrs=[row["email"] for row in emails],
                                   msg=f"Subject: New Low Price Flight!\n\n{message}\n{link}".encode("utf-8"))
            # account_sid = "ACc2e766270f4c28a1294bf59a4a837eaa"
            # auth_token = os.environ["TWILIO_TOKEN"]
            # client = Client(account_sid, auth_token)
            # message = client.messages.create(
            #     body=f"Low price alert! Only €{flightInfos.price} to fly from {flightInfos.origin_city}"
            #          f"to {flightInfos.destination_city}, from {flightInfos.out_date} to {flightInfos.return_date}.",
            #     from_="+12706336456",
            #     to=os.getenv("PHONE_NUMBER")
            # )
            # print(message.sid)
