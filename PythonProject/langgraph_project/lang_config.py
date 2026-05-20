# Import necessary libraries
# LangGraph imports (Updated based on recent versions)
# Load environment variables

from config import OPENAI_API_KEY

# Set environment variables (especially useful for LangChain integrations)
openai_api_key = OPENAI_API_KEY

print("API Keys loaded (partially hidden for security):")
print(f"OpenAI Key starts with: {openai_api_key[:5]}...")
