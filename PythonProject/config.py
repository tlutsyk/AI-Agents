import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY");

MAIN_MODEL = "gpt-4.1-mini"
SMALL_MODEL = "gpt-4.1-nano"