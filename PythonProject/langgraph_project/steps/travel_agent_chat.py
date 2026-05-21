import uuid

import gradio as gr
from langchain_core.messages import ToolMessage, AIMessage, HumanMessage

from langgraph_project.execution_flow.simple_flight_call import app_flight_search


def make_chat_fn(app_travel_agent):

    def travel_agent_chat(user_input, history):
        tools_used = []

        stream = app_travel_agent.stream(
            {"messages": [HumanMessage(content=user_input)]},
            config={"recursion_limit": 15, "configurable": {"thread_id": str(uuid.uuid4())}},
        )

        for chunk in stream:
            for node in chunk.values():
                if "messages" not in node:
                    continue

                for msg in node["messages"]:
                    if isinstance(msg, ToolMessage):
                        tools_used.append(msg.name)
                        yield f"🔧 Tool: {msg.name}\n{msg.content}\n"

                    elif isinstance(msg, AIMessage) and msg.content:
                        yield msg.content

        if tools_used:
            yield f"\n\nTools used: {', '.join(set(tools_used))}"

    return travel_agent_chat


travel_chatbot_interface = gr.ChatInterface(
    fn=make_chat_fn(app_flight_search),
    chatbot=gr.Chatbot(
        height=650,
        label="AI Travel Agent",
        render_markdown=True,
    ),

    textbox=gr.Textbox(
        placeholder="Plan your trip! Ask about attractions, flights, hotels...", container=False, scale=7
    ),
    title="✈️ LangGraph AI Travel Agent 🌍",
    description="Your stateful travel assistant…",
    examples=[
        ["What are the top 3 tourist attractions in Tokyo (HND)?"],
        ["Find flights from London (LHR) to Paris (CDG) leaving next month for 4-day trip"],
        ["Book a hotel for 5 nights in NYC next month"],
    ],
    cache_examples=False,
)

travel_chatbot_interface.launch()