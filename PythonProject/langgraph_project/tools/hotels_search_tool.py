from langchain_core.tools import tool
import requests

from config import SERPAPI_API_KEY


@tool
def search_hotels_tool(
    destination: str,
    check_in: str,
    check_out: str,
    adults: int = 2,
    currency: str = "USD",
    max_results: int = 5,
):
    """
    Search hotels using Google Hotels via SerpAPI.

    Required:
        destination – city name or place (e.g. "Prague", "Athens")
        check_in – YYYY-MM-DD
        check_out – YYYY-MM-DD

    Optional:
        adults – number of guests
        currency – pricing currency
        max_results – number of hotels to return
    """

    url = "https://serpapi.com/search.json"

    params = {
        "engine": "google_hotels",
        "q": destination,
        "check_in_date": check_in,
        "check_out_date": check_out,
        "adults": adults,
        "currency": currency,
        "hl": "en",
        "api_key": SERPAPI_API_KEY,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        hotels = data.get("properties", [])

        if not hotels:
            return f"No hotels found in {destination}."

        results = []
        for hotel in hotels[:max_results]:
            name = hotel.get("name")
            price = hotel.get("rate_per_night", {}).get("lowest")
            rating = hotel.get("overall_rating")

            results.append(
                f"{name} | ⭐ {rating} | 💰 {price} per night"
            )

        return "Found hotels:\n- " + "\n- ".join(results)

    except requests.RequestException as e:
        return f"HTTP Error: {e}\nResponse: {getattr(e.response, 'text', '')}"