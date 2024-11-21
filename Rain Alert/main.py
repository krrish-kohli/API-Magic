import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")  # Change this to your api_key
account_sid = os.environ.get("ACCOUNT_SID")  # Change this to your account_sid
auth_token = os.environ.get("AUTH_TOKEN")  # Change this to your auth_token

parameters = {
    "lat": 33.774020,  # Change this according to your location
    "lon": -118.143720,  # Change this according to your location
    "appid": api_key,  # Change this to your api_key
    "cnt": 4,
}
response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+18774555395",
        to="+15625642005",
    )

    print(message.status)
