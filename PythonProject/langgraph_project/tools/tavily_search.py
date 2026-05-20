from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

from config import MAIN_MODEL

llm = ChatOpenAI(model = MAIN_MODEL, temperature = 0, streaming = True)
print("LangChain OpenAI Chat Model configured.")

tavily_search_tool = TavilySearchResults(max_results = 3)

tools_list_single = [tavily_search_tool]