from langgraph_project.models.models import AgentState
from langgraph_project.tools.tavily_search import llm

def make_call_model_with_tools(tools: list):
    def call_model_with_tools(state: AgentState):
        print("DEBUG: Entering call_model_with_tools node")
        messages = state["messages"]

        # Binds the tools to the language model
        model_with_tools = llm.bind_tools(tools)

        # Feeds the conversation history (messages) into the model
        response = model_with_tools.invoke(messages)

        # Return the model response as a new message
        return {"messages": [response]}

    return call_model_with_tools
