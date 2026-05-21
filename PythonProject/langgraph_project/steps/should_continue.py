from typing import Literal

from langchain_core.messages import AIMessage
from langgraph.constants import END

from langgraph_project.models.models import AgentState


def should_continue(state):
    messages = state["messages"]

    # limit infinite loops (IMPORTANT)
    tool_calls_count = sum(
        1 for m in messages
        if getattr(m, "tool_calls", None)
    )

    if tool_calls_count > 5:
        return END

    last_message = messages[-1]

    # stop on tool error
    if "HTTP Error" in str(last_message.content):
        return END

    # continue only if model requests tool
    if getattr(last_message, "tool_calls", None):
        return "action"

    return END