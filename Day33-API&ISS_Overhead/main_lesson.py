import requests

# Requests the "API Endpoint" and prints status code of the request.
response = requests.get(url='http://api.open-notify.org/iss-now.json')
print(response.status_code)

# Raises status exception if response returns bad.
response.raise_for_status()

# Returns API data as dict.
data = response.json()

# Returns the 'iss_position' key of the data dict.
iss_pos = data["iss_position"]

# Returns the "latitude" key of "iss_position" dict.
iss_lat = iss_pos["latitude"]
print(iss_lat)
