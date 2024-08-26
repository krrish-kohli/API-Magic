import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 33.770050  # My latitude
MY_LONG = -118.193741  # My longitude
MY_EMAIL = "pythoncodetester4@gmail.com"
PASSWORD = "zaaizqkyqbbloetb"


def is_iss_overhead():
    """Checks if the ISS' latitude and longitude is near you."""

    # Making the GET request from the ISS API.
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # Raising an exception if unsuccessful status code is returned.
    response.raise_for_status()
    # Getting the latitude and longitude of ISS.
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])  # ISS' latitude
    iss_longitude = float(data["iss_position"]["longitude"])  # ISS' longitude

    # If my position is within +5 or -5 degrees of the ISS position.
    if MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 and MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
        return True


def is_night():
    """Checks if it's dark at your location or not."""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    # Making the GET request from the sunrise-sunset API.
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    # Raising an exception if unsuccessful status code is returned.
    response.raise_for_status()
    # Getting the sunrise and sunset time of your location.
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Getting the time at the moment.
    time_now = datetime.now().hour

    # Checking if it is dark
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    # Making the code run every 60 seconds.
    time.sleep(60)
    # Checking if ISS is near you after sunset or before sunrise.
    if is_iss_overhead() and is_night():
        # Sending the email.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Look up👆\n\nThe ISS is above you in the sky."
            )
