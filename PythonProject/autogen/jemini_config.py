# Configuration for Google Gemini Agent
# Note: Ensure GOOGLE_API_KEY is loaded correctly from your .env file
from config import GOOGLE_API_KEY

config_list_gemini = [
    {
        "model": "gemini-2.0-flash",  # Or "gemini-pro"
        "api_key": GOOGLE_API_KEY,
        "api_type": "google",  # Specify the API type for Autogen's Google integration
    }
]

llm_config_gemini = {
    "config_list": config_list_gemini,
    "temperature": 0.6,  # Maybe slightly less randomness for strategic Chief Marketing Officer
    "timeout": 120,
}