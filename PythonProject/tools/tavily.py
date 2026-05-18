from typing_extensions import TypedDict

import requests
from agents import function_tool
from config import TAVILY_API_KEY

# Define the Tavily search function
class TavilyParams(TypedDict):
    query: str
    max_results: int

@function_tool
def tavily_search(params: TavilyParams) -> str:
    """Return a newline‑joined summary of Tavily results."""
    url = "https://api.tavily.com/search"
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": params["query"],
        "max_results": params.get("max_results", 3),
    }
    resp = requests.post(url, json = payload, headers = {"Content-Type": "application/json"})
    if resp.status_code != 200:
        return f"Tavily error {resp.status_code}"
    items = resp.json().get("results", [])
    return "\n".join([f"- {itm['title']}: {itm['content']}" for itm in items]) or "No hits"
