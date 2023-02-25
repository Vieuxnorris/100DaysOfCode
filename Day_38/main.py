from utils import *
import requests


def postNutritionixApi():
    JSON_EXERCISE_END_POINT["query"] = input("tell me which exercises you did: ")
    with requests.post(url=EXERCISE_END_POINT, headers=HEADERS_EXERCISE_END_POINT, json=JSON_EXERCISE_END_POINT) \
            as exercise:
        exercise.raise_for_status()
        googleSheetPost(exercise.json())


def googleSheetPost(arg_exerciseJson: dict):
    jsonExercise = {
        "feuille1":
        {
            "date": DATE,
            "time": DATE_TIME,
            "exercise": arg_exerciseJson["exercises"][0]["user_input"].title(),
            "duration": arg_exerciseJson["exercises"][0]["duration_min"],
            "calories": arg_exerciseJson["exercises"][0]["nf_calories"],
        }
    }
    with requests.post("https://api.sheety.co/cb9aae7ba107a14822530821c1301289/workouts/feuille1",
                       json=jsonExercise, headers=HEADER_SHEETY) as postRow:
        postRow.raise_for_status()
        print(postRow.json())

postNutritionixApi()