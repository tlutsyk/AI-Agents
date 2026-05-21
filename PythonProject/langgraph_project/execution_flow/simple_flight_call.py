from langgraph_project.execution_flow.app_call import app_call
from langgraph_project.grapths.one_tool import build_graph_one_tool
from langgraph_project.tools.get_current_date_tool import get_current_date_tool
from langgraph_project.tools.hotels_search_tool import search_hotels_tool
from langgraph_project.tools.search_flights_tool import search_flights_tool
from langgraph_project.tools.tavily_search import tavily_search_tool

# Tool list
tools_list_full = [
    tavily_search_tool,
    search_flights_tool,
    get_current_date_tool,
    search_hotels_tool,
]
# Build graph
app_flight_search = build_graph_one_tool(
    tools_list_full
)

# Prepare your input
prompt = ("I want the latest news about Athens. I'm planning to visit a fly from Prague to Athens in dates 2026-06-15 - 2026-06-21."
          "It's round trip. Can you find cheap flight options for 2 adults and fetch security and travel advisories? Also finf"
          "a hotel in Athens prefer balance between price and rating higher than 4.5 in the city center."
          "Finally, format the combined output.")

output, history = app_call(app_flight_search, prompt)

print("\n==================== OUTPUT ====================")
print(output)

print("\n==================== HISTORY ===================")
print(history)