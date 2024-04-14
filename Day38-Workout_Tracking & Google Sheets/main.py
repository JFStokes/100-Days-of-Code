#####################################################################
#                         WORKOUT TRACKER                           #
#####################################################################
# OVERVIEW - A workout tracker using Nutritionix API and Google Sheets.
import datetime
import json
import os
import requests

DIR_PATH = os.path.dirname(__file__)

# TODO 1 - Setup API Credentials and Google Sheet.
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
USER_NAME = "jfstokes"
API_ID = "0acb2c25"
API_KEY = "1de66b2941723d4cd2eeef769a15177f"
WEIGHT = 75
HEIGHT = 175
AGE = 35
SHEET_ENDPOINT = "https://api.sheety.co/e737331eab80bd9b309b99e5f565566d/workoutTracker/workouts"
SHEET_USER_NAME = "JFStokes"
SHEET_PW = "JMsl2008$%"

# TODO 2 - Get Exercise Stats with Natural Language Queries.
exercise = input("--> Exercise: ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
    }

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=parameters, headers=headers)
result = response.json()

# Save JSON data to text file.
with open(f"{DIR_PATH}/result.txt", mode="a") as file:
    file.write(str(result))

# Save JSON data to JSON file.
with open(f"{DIR_PATH}/result.json", "w") as file:
    json.dump(result, file, indent=4, separators=(",", ": "))

# TODO 3 - Setup Google Sheet with Sheety.

# TODO 4 - Save data to Google Sheet.
today = datetime.datetime.now().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%X")

# Dict containing data for sheet.
sheet_inputs = {
    "workout": {
        "date": today,
        "time": time,
        "exercise": result["exercises"][0]["name"].title(),
        "duration": result["exercises"][0]["duration_min"],
        "calories": result["exercises"][0]["nf_calories"]
    }
}

# Header dictionary.
headers = {

}

response = requests.post(
    url=SHEET_ENDPOINT, 
    json=sheet_inputs,
    auth=(
        SHEET_USER_NAME,
        SHEET_PW
    )
)
print(response.text)

# TODO 5 - Authenticate Sheety API.

# TODO 6 - Environment Variables in Repl.it.

#####################################################################
