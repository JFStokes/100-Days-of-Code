import requests
from datetime import datetime

# Declare constants.
USERNAME = "jfstokes"
TOKEN = "xNadW9$a8$0c7#VOy!in"
GRAPH_ID = "graph1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ENDPOINT2 = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
GRAPH_UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/"

# Required params for POST request to pixe.la. 
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Send POST request to create a user account.
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

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

# Send POST request to create a graph.
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

# Gets today's datetime.
today = datetime.now()

# graph_data = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "3.0"
# }

# Send POST request to send data to the graph.
# response = requests.post(url=GRAPH_ENDPOINT2, json= graph_data, headers=headers)
# print(response.text)

# Send UPDATE request to change previous data
date = input("--> Date(yyyymmdd): ")
amount = input("--> Amount: ")

graph_data = {
    "quantity": amount
}

# https://pixe.la/v1/users/jfstokes/graphs/graph1.html
response = requests.put(url=GRAPH_UPDATE_ENDPOINT + date, json=graph_data, headers=headers)
print(response.text)
