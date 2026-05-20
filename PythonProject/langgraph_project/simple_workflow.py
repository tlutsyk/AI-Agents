# Langchain specific imports
from langgraph.graph import StateGraph

from langgraph_project.state import AgentState

from langgraph_project.steps.translation_step import translation_step
from langgraph_project.steps.sentiment_step import analyze_sentiment_step
from langgraph_project.steps.summarize_step import summarize_step

# Langchain specific imports

# Let's define a stategraph with the "AgentState" we defined earlier
workflow = StateGraph(AgentState)

# Let's add a node, which is the summarize function we defined before
workflow.add_node("summarize", summarize_step)
workflow.add_node("translation", translation_step)
workflow.add_node("sentiment_check", analyze_sentiment_step)

# Let's define Edges, which define how data flows between nodes
workflow.add_edge("summarize", "translation")
workflow.add_edge("translation", "sentiment_check")
#workflow.add_edge("translation", END)
workflow.set_entry_point("summarize")
workflow.compile()