import requests
from datetime import datetime

# Declare constants.
USERNAME = ""
TOKEN = ""
GRAPH_ID = ""
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

# Required params for POST request to pixe.la. 
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Send POST request.
response = requests.post(url=PIXELA_ENDPOINT, json=user_params)

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
