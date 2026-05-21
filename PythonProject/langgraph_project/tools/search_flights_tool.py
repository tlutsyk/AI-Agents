# pip install requests langchain

import os
import requests

from langchain.tools import tool

from config import SERPAPI_API_KEY


@tool
def search_flights_tool(
    origin_code: str,
    destination_code: str,
    departure_date: str,
    return_date: str | None = None,
    adults: int = 1,
    travel_class: str = "economy",
    currency: str = "USD",
    max_offers: int = 5,
):
    """
    Search flights using Google Flights via SerpAPI.

    Required:
        origin_code, destination_code – IATA airport/city codes
        departure_date – YYYY-MM-DD

    Optional:
        return_date – round trip
        adults – number of passengers
        travel_class – economy, premium_economy, business, first
        currency – USD, EUR, etc.
        max_offers – max returned offers
    """

    try:

        url = "https://serpapi.com/search.json"

        params = {
            "engine": "google_flights",
            "departure_id": origin_code.upper(),
            "arrival_id": destination_code.upper(),
            "outbound_date": departure_date,
            "currency": currency,
            "hl": "en",
            "api_key": SERPAPI_API_KEY,
        }

        # Optional params
        if return_date:
            params["return_date"] = return_date

        if adults:
            params["adults"] = adults

        # Google Flights class mapping
        class_map = {
            "ECONOMY": 1,
            "PREMIUM_ECONOMY": 2,
            "BUSINESS": 3,
            "FIRST": 4,
            "economy": 1,
            "premium_economy": 2,
            "business": 3,
            "first": 4,
        }

        params["travel_class"] = class_map.get(
            travel_class,
            1
        )

        print(
            f"DEBUG: Searching flights "
            f"{origin_code} -> {destination_code}"
        )

        response = requests.get(
            url,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        # Best flights section
        flights = (
            data.get("best_flights", [])
            or data.get("other_flights", [])
        )

        if not flights:
            return (
                f"No flights found for "
                f"{origin_code} → {destination_code}"
            )

        results = []

        for flight in flights[:max_offers]:

            price = flight.get("price", "N/A")

            total_duration = flight.get(
                "total_duration",
                "N/A"
            )

            flights_list = flight.get("flights", [])

            if not flights_list:
                continue

            first_leg = flights_list[0]
            last_leg = flights_list[-1]

            airline = first_leg.get(
                "airline",
                "Unknown Airline"
            )

            dep_airport = (
                first_leg
                .get("departure_airport", {})
                .get("id", origin_code)
            )

            arr_airport = (
                last_leg
                .get("arrival_airport", {})
                .get("id", destination_code)
            )

            dep_time = (
                first_leg
                .get("departure_airport", {})
                .get("time", "N/A")
            )

            arr_time = (
                last_leg
                .get("arrival_airport", {})
                .get("time", "N/A")
            )

            result = f"""
Airline: {airline}
Route: {dep_airport} → {arr_airport}
Departure: {dep_time}
Arrival: {arr_time}
Duration: {total_duration} min
Price: {price} {currency}
            """.strip()

            results.append(result)

        if not results:
            return "No valid flight results parsed."

        return "\n\n".join(results)

    except requests.HTTPError as e:

        return f"""
HTTP Error:
{str(e)}

Response:
{response.text}
        """.strip()

    except Exception as e:

        return f"Unexpected error: {str(e)}"
