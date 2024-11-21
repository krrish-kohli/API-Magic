import requests
from datetime import datetime
import os

# TRY TO RUN IT WITH HARDCORE VALUES OF KEYS FIRST

APP_ID = os.environ.get("APP_ID") # add your own
API_KEY = os.environ.get("API_KEY") # add your own
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT") # add your own
TOKEN = os.environ.get("TOKEN") # add your own

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

nutrionix_parameters = {
    "query": str(input("Tell me which exercises you did: ")),
}

# Converts the text input into duration, calories, and other things according to the excel sheet
nutrionix_response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=nutrionix_parameters, headers=headers)
# print(nutrionix_response.text)

sheety_headers = {
    "Authorization": TOKEN,
}

result = nutrionix_response.json()

# Updates the excel sheet
for exercise in result["exercises"]:
    data = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_response = requests.post(url=SHEET_ENDPOINT, json=data, headers=sheety_headers)
    print(sheety_response.text)
