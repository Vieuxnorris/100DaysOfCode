import os
import datetime as dt

EXERCISE_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
DATE = dt.datetime.now().strftime("%d/%m/%Y")
DATE_TIME = dt.datetime.now().strftime("%H:%M:%S")

HEADERS_EXERCISE_END_POINT = {
    "x-app-id": os.getenv("API_ID"),
    "x-app-key": os.getenv("API_KEY"),
    "Content-Type": "application/json",
}

HEADER_SHEETY = {
    "Authorization": os.getenv("TOKEN")
}

JSON_EXERCISE_END_POINT = {
    "query": "",
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 25
}
