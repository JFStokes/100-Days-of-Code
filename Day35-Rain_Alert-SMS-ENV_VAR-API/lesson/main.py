import pytemp
import requests

API_KEY = "830b802c164c79fb1432e95915cd223f"
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": 34.823540,
    "lon": -89.994118,
    "appid": API_KEY,
    "cnt": 4,
    "units": "imperial"
}

response = requests.get(API_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

print(f'{API_ENDPOINT}?lat={parameters["lat"]}&lon={parameters["lon"]}\
&appid={parameters["appid"]}&cnt={parameters["cnt"]}&units={parameters["units"]}')

weather_codes = []

for n in range(0, 4):
    day_data = data["list"][n]["weather"]
    code = day_data[0]["id"]
    weather_codes.append(code)

print(weather_codes)

will_rain = False

for c in weather_codes:
    if c < 700:
        will_rain = True
        break
    else:
        continue

if will_rain:
    print('Bring an umbrella.')
else:
    print('No rain!')
