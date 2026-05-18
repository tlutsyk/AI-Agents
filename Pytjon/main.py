import os, requests, asyncio
from IPython.display import display, Markdown
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, SQLiteSession
from pydantic import BaseModel
from typing_extensions import TypedDict
from datetime import datetime
from agents import RunResult  # Make sure RunResult is imported
# from helper import format_report_to_markdown
from agents import handoff, RunContextWrapper, CodeInterpreterTool, input_guardrail, GuardrailFunctionOutput, TResponseInputItem
from agents.extensions import handoff_filters
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")