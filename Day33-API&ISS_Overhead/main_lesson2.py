import datetime as dt
import requests

# Varaible for today & current time.
today = dt.datetime.now()

# Sets parameters per API docs.
parameters = {
    'lat': 34.823540,
    'lng': -89.994118,
    'formatted': 0,
    'tzid': 'America/Chicago'
}

# Gets API endpoint & enters parameters.
response = requests.get(url='https://api.sunrise-sunset.org/json', 
                        params=parameters
                        )

# Stores API in data variable.
data = response.json()

# Gets response status code.
response.raise_for_status()

# Sunrise variable = data/results/sunrise/T/1/:/0.
sr = data["results"]["sunrise"].split('T')[1].split(':')[0]

# Sunset variable = data/results/sunset/T/1/:/0.
ss = data["results"]["sunset"].split('T')[1].split(':')[0]

print(f'--> Sunrise: {sr}')
print(f'--> Sunset: {ss}')
