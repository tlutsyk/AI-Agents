# Let's create our agents using different models
# Create the Chief Marketing Officer Agent now using Google Gemini
import autogen

from autogen_config import llm_config_openai
from jemini_config import llm_config_gemini
from planner_agents import cmo_prompt, brand_marketer_prompt

cmo_agent_gemini = autogen.ConversableAgent(
    name = "Chief_Marketing_Officer_Gemini",
    system_message = cmo_prompt,
    llm_config = llm_config_gemini,  # Assign the Gemini config!
    human_input_mode = "NEVER")

# Create the Brand Marketer Agent using OpenAI GPT (this is similar to before!)
# We can reuse the llm_config_openai defined earlier
brand_marketer_agent_openai_mixed = autogen.ConversableAgent(
    name = "Brand_Marketer_OpenAI",  # Keep name consistent if desired, or update
    system_message = brand_marketer_prompt,
    llm_config = llm_config_openai,  # Assign the OpenAI config!
    human_input_mode = "NEVER")

print(f"Agent '{cmo_agent_gemini.name}' created (using Google Gemini).")
print(f"Agent '{brand_marketer_agent_openai_mixed.name}' created (using OpenAI).")