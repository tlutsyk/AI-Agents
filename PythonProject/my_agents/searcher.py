from agents import Agent
from schemas.summary import Summary
from hooks.print_hooks import print_hooks
from config import MAIN_MODEL
from tools.tavily import tavily_search

search_agent = Agent(name = "Searcher",
                     instructions = """Context: You are a search specialist agent with access to the Tavily web search tool. 
        Your goal is to provide up-to-date, relevant information for a research task. 
        Instruction: Use Tavily search to find the most recent and pertinent information related to the user's query. 
        Summarize your findings clearly and concisely in no more than 200 words. 
        Input: The user's search query. 
        Output: A concise summary (≤200 words) of the most relevant and recent information found via Tavily search.""",
                     tools = [tavily_search],
                     model = MAIN_MODEL,
                     hooks = print_hooks,
                     output_type = Summary)