from datetime import datetime

from agents import Agent
from config import MAIN_MODEL
from schemas.search_plan import SearchPlan
from guards.military_guardrail import military_guardrail

date = datetime.now().strftime('%Y-%m-%d')

planner_agent = Agent(name = "Planner test",
                      instructions = f"""Current date: {date} \n Context: You are a research planner agent tasked with designing a comprehensive research plan for a user request. 
        You have access to web search tools and should utilize the current date ({date}) when planning. 
        Instruction: Break down the user's request into 3 distinct web searches, each with a clear reason and a specific query. 
        Ensure coverage of recent news, company fundamentals, risks, sentiment, and broader context. 
        Input: The user's research request and the current date. 
        Output: A list of search plan items, each with a 'reason' and a 'query', formatted as a JSON object matching the SearchPlan schema.""",
                      model = MAIN_MODEL,
                      output_type = SearchPlan,
                      input_guardrails = [military_guardrail]) # THIS IS THE GUARDRAIL THAT PREVENTS POLITICAL TOPIC ASKS
