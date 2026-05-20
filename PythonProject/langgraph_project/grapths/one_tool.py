from IPython.core.display_functions import display
from langgraph.constants import END
from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode

from langgraph_project.models.models import AgentState
from langgraph_project.steps.make_call_model_with_tools import make_call_model_with_tools
from langgraph_project.steps.should_continue import should_continue


def build_graph_one_tool(tools_list):
    # Let's Instantiate ToolNode
    tool_node = ToolNode(tools_list)

    # Define the call_node_fn, which binds the tools to the LLM and calls OpenAI API
    call_node_fn = make_call_model_with_tools(tools_list)

    # Build the Graph with One Tool using ToolNode
    graph_one_tool = StateGraph(AgentState)

    # Add nodes
    graph_one_tool.add_node("agent", call_node_fn)

    # Add the ToolNode instance directly, naming it "action"
    graph_one_tool.add_node("action", tool_node)

    # Set entry point
    graph_one_tool.set_entry_point("agent")

    # Add a conditional edge from the agent
    # The dictionary maps the return value of 'should_continue' ("action" or END)
    # to the name of the next node ("action" or the special END value).
    graph_one_tool.add_conditional_edges(
        "agent",  # Source node name
        should_continue,  # Function to decide the route
        {"action": "action", END: END},  # Mapping: {"decision": "destination_node_name"}
    )

    # Add edge from action (ToolNode) back to agent
    graph_one_tool.add_edge("action", "agent")

    # Compile the graph
    app = graph_one_tool.compile()

    # Visualize
    from IPython.display import Image, display

    display(Image(app.get_graph().draw_mermaid_png()))

    return app