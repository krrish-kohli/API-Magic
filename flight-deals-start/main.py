import time
from data_manager import DataManager
from flight_search import FlightSearch
import flight_data
from notification_manager import NotificationManager

# ==================== Retrieving the sheet data=======================
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_sheet_data()
# print(sheet_data)

# ==================== Updating the IATA code for the places in Google Sheet =======================
if sheet_data[0]["iataCode"] == "":
    for sheet in sheet_data:
        sheet["iataCode"] = flight_search.update_iata(sheet["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_sheet_data()

# ==================== Searching for the cheapest flight and sending SMS =======================
for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.flight_prices("LAX", destination['iataCode'])
    cheapest_flight = flight_data.find_cheapest_flight(flights)
    print(f"{destination['city']}: ${cheapest_flight.price}")
    time.sleep(2)

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        notification_manager.send_message(message_body=f"Low price alert! Only {cheapest_flight.price} to fly "
                                                       f"from {cheapest_flight.origin_airport} "
                                                       f"to {cheapest_flight.destination_airport}, on "
                                                       f"{cheapest_flight.out_date} "
                                                       f"until {cheapest_flight.return_date}.")
