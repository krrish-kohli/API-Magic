import time
from data_manager import DataManager
from flight_search import FlightSearch
import flight_data
from notification_manager import NotificationManager

# Link for adding yourself as a user: https://docs.google.com/forms/d/e/1FAIpQLSely-_OMxh5SFnKL8hVvZhHIvIGHrKsHGojjd_3ELf3ckYYvQ/viewform?usp=sf_link
# Link for adding more airports to the sheet: https://docs.google.com/spreadsheets/d/1nZmN_7PmAi9Hop7_hNs4y2mdq-P_dOfYXGA_mLv4oFU/edit?gid=0#gid=0

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

# ==================== Retrieving customer emails =======================
customer_data = data_manager.get_customer_emails()
# Retrieving the emails from all the responses
customer_email_list = [row["whatIsYourEmail?"] for row in customer_data]

# ==================== Searching for the cheapest direct flight =======================
for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.flight_prices("LAX", destination['iataCode'])
    cheapest_flight = flight_data.find_cheapest_flight(flights)
    print(f"{destination['city']}: ${cheapest_flight.price}")
    time.sleep(2)

# ==================== Updating the IATA code for the places in Google Sheet =======================
    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.flight_prices("LAX", destination['iataCode'])
        cheapest_flight = flight_data.find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price is: ${cheapest_flight.price}")
        time.sleep(2)

# ==================== Sending sms and emails=======================
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        if cheapest_flight.stops == 0:
            notification_manager.send_message(message_body=f"Low price alert! Only ${cheapest_flight.price} to fly "
                                                           f"from {cheapest_flight.origin_airport} "
                                                           f"to {cheapest_flight.destination_airport}, on "
                                                           f"{cheapest_flight.out_date} "
                                                           f"until {cheapest_flight.return_date}.")
            notification_manager.send_emails(users=customer_email_list, body=f"Low price alert! "
                                                                             f"Only ${cheapest_flight.price} to fly "
                                                                             f"from {cheapest_flight.origin_airport} "
                                                                             f"to {cheapest_flight.destination_airport}"
                                                                             f", on {cheapest_flight.out_date} "
                                                                             f"until {cheapest_flight.return_date}.")
        else:
            notification_manager.send_message(message_body=f"Low price alert! "
                                                           f"Only ${cheapest_flight.price} to fly "
                                                           f"from {cheapest_flight.origin_airport} "
                                                           f"to {cheapest_flight.destination_airport} "
                                                           f"with {cheapest_flight.stops} stop(s) "
                                                           f", on {cheapest_flight.out_date} "
                                                           f"until {cheapest_flight.return_date}.")
            notification_manager.send_emails(users=customer_email_list, body=f"Low price alert! "
                                                                             f"Only ${cheapest_flight.price} to fly "
                                                                             f"from {cheapest_flight.origin_airport} "
                                                                             f"to {cheapest_flight.destination_airport}"
                                                                             f" with {cheapest_flight.stops} stop(s) "
                                                                             f", on {cheapest_flight.out_date} "
                                                                             f"until {cheapest_flight.return_date}.")
