from typing import Literal

from langchain_core.messages import AIMessage
from langgraph.constants import END

from langgraph_project.models.models import AgentState


def should_continue(state: AgentState) -> Literal["action", "__end__"]:
    """Determines the next step: continue with tools or end."""
    print("DEBUG: Entering should_continue node")
    last_message = state["messages"][-1]

    # Check if the last message is an AIMessage with tool_calls
    if isinstance(last_message, AIMessage) and hasattr(last_message, "tool_calls") and last_message.tool_calls:
        print("DEBUG: Decision: continue (route to action)")
        return "action"  # Route to the node named "action"
    else:
        print("DEBUG: Decision: end (route to END)")
        return END  # Special value indicating the end of the graph