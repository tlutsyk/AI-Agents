from langchain_core.messages import HumanMessage

from helpers.print_markdown import print_markdown
from langgraph_project.grapths.one_tool import build_graph_one_tool
from langgraph_project.tools.tavily_search import tools_list_single


def app_call(app, messages):
    # Initialize the state with the provided messages
    initial_state = {"messages": [HumanMessage(content=messages)]}

    # Invoke the app with the initial state
    final_state = app.invoke(initial_state)

    # Iterate through the messages in the final state
    for i in final_state["messages"]:
        # Print the type of the message in markdown format
        print_markdown(i.type)
        # Print the content of the message in markdown format
        print_markdown(i.content)
        # Print any additional kwargs associated with the message
        if i.additional_kwargs != {}:
            print(i.additional_kwargs)

    # Return the content of the last message and the final state
    return final_state["messages"][-1].content, final_state

#app = build_graph_one_tool(tools_list_single)

#messages = "What's the latest news on Ukraine in May 2026? Is it a good time to visit?"
#output, history = app_call(app, messages)

#print("\n==================== OUTPUT ====================")
#print(output)

#print("\n==================== HISTORY ===================")
#print(history)