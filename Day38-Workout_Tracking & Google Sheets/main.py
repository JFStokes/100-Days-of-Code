#####################################################################
#                         WORKOUT TRACKER                           #
#####################################################################
# OVERVIEW - A workout tracker using Nutritionix API and Google Sheets.
import requests

# TODO 1 - Setup API Credentials and Google Sheet.
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
USER_NAME = "jfstokes"
API_ID = "0acb2c25"
API_KEY = "1de66b2941723d4cd2eeef769a15177f"

# TODO 2 - Get Exercise Stats with Natural Language Queries.
exercise = input("--> Exercise: ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise
}

response = requests.get(url=NUTRITIONIX_ENDPOINT, params=parameters, headers=headers)
print(response.text)

# TODO 3 - Setup Google Sheet with Sheety.

# TODO 4 - Save data to Google Sheet.

# TODO 5 - Authenticate Sheety API.

# TODO 6 - Environment Variables in Repl.it.

#####################################################################
