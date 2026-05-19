from config import OPENAI_API_KEY

config_list_openai = [
    {
        "model": "gpt-4o-mini",
        "api_key": OPENAI_API_KEY,
    }
]

llm_config_openai = {
    "config_list": config_list_openai,
    "temperature": 0.7,  # Use a slightly higher temp for creative marketing ideas
    "timeout": 120,
}