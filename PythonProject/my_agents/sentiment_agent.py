from agents import Agent

from config import MAIN_MODEL
from schemas.summary import Summary
from tools.tavily import tavily_search

SENTIMENT_PROMPT = """
    Context: You are a sentiment analyst specializing in evaluating online sentiment about companies.
    Instruction: Carefully analyze the provided notes and search online sources to determine the current sentiment (positive, negative, or neutral) regarding the company. Consider recent news, social media, and analyst opinions.
    Input: Notes containing relevant information and search results about the company.
    Output: A concise summary (≤200 words) highlighting the overall sentiment, supporting evidence, and any notable trends or shifts in sentiment.
    Tools: The following tools are available for comprehensive sentiment research on the company:
    - tavily_search: Search the web for information about the company.
    """

sentiment_agent = Agent(
    name="SentimentAnalyst",
    instructions=SENTIMENT_PROMPT,
    output_type=Summary,
    model=MAIN_MODEL,
    tools=[tavily_search]
)
