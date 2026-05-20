from typing_extensions import TypedDict

class AgentState(TypedDict):
    input_text: str
    summary: str
    translation: str
    sentiment_marker: str