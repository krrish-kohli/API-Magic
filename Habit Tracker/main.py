import requests
import os
from datetime import datetime

USERNAME = "krrishkohli"
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = "graph"

headers = {
    "X-USER-TOKEN": TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Study Graph",
    "unit": "hrs",
    "type": "float",
    "color": "momiji",
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

yesterday = datetime(year=2024, month=10, day=8).strftime("%Y%m%d")
today = datetime.now().strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": input("How many hours did you study today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixel_creation_endpoint}/{yesterday}"

update_data = {
    "quantity": "2",
}

# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

tomorrow = datetime(year=2024, month=10, day=10).strftime("%Y%m%d")

delete_endpoint = f"{pixel_creation_endpoint}/{tomorrow}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
