class FlightData:
    """This class is responsible for structuring the flight data."""
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date


def find_cheapest_flight(data):
    """This function parses the JSON file to check for cheaper prices and returns it along with the flight details."""

    # Handles empty data.
    if data is None or not data['data']:
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    # Data of the first flight in the JSON.
    first_flight = data['data'][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

    # Checks if the other flights have cheaper prices available than the first flight.
    for flight in data['data']:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

    return cheapest_flight
