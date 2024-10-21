import requests
import os
from dotenv import load_dotenv

# Loading environment variables
load_dotenv()


class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self):
        self.token = os.getenv('TOKEN')
        self.sheet_endpoint = os.getenv('SHEET_ENDPOINT')
        self.destination_data = {}

        self.sheety_headers = {
            "Authorization": self.token,
        }

    def get_sheet_data(self):
        """This function helps in getting all the data in the sheet."""

        # Using the Sheety API to get all the data from the sheet.
        sheety_response = requests.get(url=self.sheet_endpoint, headers=self.sheety_headers)
        data = sheety_response.json()
        # Adding the data of the sheet in destination data in JSON format.
        self.destination_data = data["prices"]
        return self.destination_data

    def update_sheet_data(self):
        """This function helps in updating the sheet data."""
        for i in self.destination_data:
            parameters = {
                "price": {
                    "iataCode": i["iataCode"]
                }
            }
            # Using the Sheety API to update the sheet.
            new_sheety_response = requests.put(url=f"{self.sheet_endpoint}/{i['id']}", json=parameters,
                                               headers=self.sheety_headers)
            print(new_sheety_response.text)
