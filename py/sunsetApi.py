import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "phoniedev2000@gmail.com"
MY_PWD = "dskbtziwjswnhgdl"
MY_LAT = 13.9466607 #nontaburi, thailand
MY_LONG = 100.4556015


def is_iss_overhead():
    #pos + - 5 degree == OK
    print(f'lat {MY_LAT - 5} - {MY_LAT + 5} lon {MY_LONG-5} - {MY_LONG+5}')
    print(f'lat:{iss_lat} lon:{iss_lon}')
    
    if MY_LAT - 5 <= iss_lat <= MY_LAT +5 and MY_LONG-5 <= iss_lon <= MY_LONG+5:
        
        return True

def is_night():

    parameters ={
        "lat" : MY_LAT,
        "lon": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now

    if time_now>= sunset or time_now <= sunrise:
        return True


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

iss_lon = float(data["iss_position"]["longitude"])
iss_lat = float(data["iss_position"]["latitude"])

iss_pos = (iss_lon, iss_lat)

#if iss is close to current pos and it currently dark 
#send email 
while True:
    time.sleep(5)
    if is_iss_overhead() and is_night():
        print("its near!")
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(MY_EMAIL, MY_PWD)
        from_addr = MY_EMAIL,
        to_addr = MY_EMAIL,
        msg = "Subject: Lookup\n\n ISS is above you !."
    else:
        print("nahh") 
        is_iss_overhead()