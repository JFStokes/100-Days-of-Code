import datetime as dt
import requests
import smtplib
import time


MY_LAT = 34.823540 # Your latitude
MY_LONG = -89.994118 # Your longitude

lat_u5 = float(MY_LAT + 5)
lat_d5 = float(MY_LAT - 5)
lon_u5 = float(MY_LONG + 5)
lon_d5 = float(MY_LONG - 5)
lat_close = False
lon_close = False
is_close = False
is_dark = False


#-------------------------> ENDLESS LOOP <--------------------------#
print('--> Starting ISS Check script.')
while True:
    time.sleep(60) # Runs code every 60 seconds.
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "America/Chicago"
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now().hour

    #If the ISS is close to my current position
    if iss_latitude < lat_u5 and iss_latitude > lat_d5:
        print(f'--> My LAT: {MY_LAT}. ISS LAT: {iss_latitude}. ISS LAT is close!')
        lat_close = True
        if iss_longitude < lon_u5 and iss_longitude > lon_d5:
            print(f'--> My LONG: {MY_LONG}. ISS LONG: {iss_longitude}. ISS LONG is close!')
            lon_close = True
        else:
            print(f'--> My LONG: {MY_LONG}. ISS LONG: {iss_longitude}. ISS LONG is not close...')
            lon_close = False
    else:
        print(f'--> My LAT: {MY_LAT}. ISS LAT: {iss_latitude}. ISS LAT is not close...')
        lat_close = False

    if lat_close and lon_close:
        is_close = True
    else:
        is_close = False

    # and it is currently dark
    if time_now > sunset or time_now < sunrise:
        print(f'--> Time: {time_now}. Sunsrise: {sunrise}. Sunset: {sunset}. It is dark!')
        is_dark = True
    else:
        print(f'--> Time: {time_now}. Sunsrise: {sunrise}. Sunset: {sunset}. It is not dark...')
        is_dark = False

    # Then send me an email to tell me to look up.
    my_email = 'joshua.f.stokes.mil@gmail.com'
    my_pw = 'cgfhzcjcgcazjvoo'
    to_email1 = 'joshua.stokes1617@yahoo.com'

    if is_close and is_dark:
        print('--> Sending email!')
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            print('--> TLS connection complete. Logging into account.')
            connection.login(user=my_email, password=my_pw)
            print('--> Login successful. Sending email.')
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email1,
                msg='Subject: ISS\n\nLOOK UP! The ISS is above you!'
            )
            print('--> Email Sent.')
    else:
        print('--> Not sending email...')

# End script.
print('--> Ending ISS Check script.')
