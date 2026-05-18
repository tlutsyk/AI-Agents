import asyncio
from datetime import datetime

import requests
from IPython.display import display, Markdown
from agents import SQLiteSession, Runner
# from helper import format_report_to_markdown
from pydantic import BaseModel

from my_agents.writer import writer_agent

# Define the models that we want to use
#session = SQLiteSession("session");

#date = datetime.now().strftime("%Y-%m-%d");
#async def main():
    # Let's test the AI Agent
  #  q2 = "Do a deep dive on the latest news in Tesla stock. I also need the fundamental analysis of the company"
 #   run1 = await Runner.run(starting_agent = writer_agent, input = q2)
 #   print(f"### 🤖 Agent’s Answer\n{run1.final_output}")

#asyncio.run(main())

#print("The end")
