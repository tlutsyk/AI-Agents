# Let's define the key node, which represents the functions that perform specific tasks in your graph
# They receive the current state and return a modified state
# Note that a node can be simple functions, LLM calls, or complex agents
from langgraph_project.lang_config import openai_api_key
from langgraph_project.state import AgentState
from langchain_openai import ChatOpenAI
from pydantic import BaseModel  # For tool args schema if needed explicitly

def translation_step(state: AgentState) -> AgentState:
    """Create a concise summary of the input text."""

    # Initialize the OpenAI model and define the prompt
    llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key)
    prompt = f"Classify the translated text as either positive, negative, or neutral: {state['summary']}"

    # Get the summary directly from the model
    result = llm.invoke([prompt])

    # Update the state with our summary
    return {
        "input_text": state["input_text"],  # Keep the original text
        "summary": state["summary"],  # Keep original summary
        "translation": state["translation"],  # Add the translation
        "sentiment_marker": result.content
    }