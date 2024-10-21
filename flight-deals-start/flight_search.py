import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Loading environment variables.
load_dotenv()

IATA_ENDPOINT = os.getenv('IATA_ENDPOINT')
TOKEN_ENDPOINT = os.getenv('TOKEN_ENDPOINT')
FLIGHT_ENDPOINT = os.getenv('FLIGHT_ENDPOINT')


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""
    def __init__(self):
        self._api_key = os.getenv('API_KEY')
        self._api_secret = os.getenv('API_SECRET')
        self._token = self._get_new_token()

    def _get_new_token(self):
        """This function generates the authentication token used for accessing the Amadeus API and returns it."""
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        return response.json()["access_token"]

    def update_iata(self, city_name):
        """This function retrieves the IATA code for a specified city using Amadeus API."""
        headers = {
            "Authorization": f"Bearer {self._token}"
        }

        body = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        # Using the Amadeus API to retrieve the IATA code.
        response = requests.get(url=IATA_ENDPOINT, params=body, headers=headers)
        # Handles the exception if the IATA code is not found.
        try:
            iata = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return iata

    def flight_prices(self, arrival, destination):
        """This function searches for the flight options from the specified arrival and destination place."""
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        # Assigning the departure date as tomorrow and return date as 6 months from now.
        departure_date = datetime.now() + timedelta(days=1)
        return_date = departure_date + timedelta(days=180)

        params = {
            "originLocationCode": arrival,
            "destinationLocationCode": destination,
            "adults": 1,
            "departureDate": departure_date.strftime("%Y-%m-%d"),
            "returnDate": return_date.strftime("%Y-%m-%d"),
            "currencyCode": "USD",
            "max": "10",
        }
        # Using the Amadeus API to get the different flight options.
        response = requests.get(url=FLIGHT_ENDPOINT, params=params, headers=headers)
        return response.json()
