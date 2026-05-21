from langchain.tools import tool
from datetime import date

from langgraph_project.execution_flow.app_call import app_call
from langgraph_project.grapths.one_tool import build_graph_one_tool


@tool
def get_current_date_tool():
    """Returns the current date in 'YYYY-MM-DD' format. Useful for finding flights/hotels relative to today."""
    return date.today().isoformat()

#app_current_date = build_graph_one_tool([get_current_date_tool])

# Prepare your input

#prompt = "What is the current date?"
#output, history = app_call(app_current_date, prompt)