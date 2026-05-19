import warnings

import autogen

from autogen_config import llm_config_openai

warnings.filterwarnings("ignore")

# Let's create Agents (Both using OpenAI initially)
# Create the Chief Marketing Officer (CMO) Agent - Using OpenAI for now

cmo_prompt = """You are the Chief Marketing Officer (CMO) of a new shoe brand (sustainable).
Provide high-level strategy, define target audiences, and guide the Marketer. Focus on the big picture. Be concise."""

cmo_agent_openai = autogen.ConversableAgent(
    name = "Chief_Marketing_Officer_OpenAI",
    system_message = cmo_prompt,
    llm_config = llm_config_openai,  # Assign the OpenAI config
    human_input_mode = "NEVER")

print(f"Agent '{cmo_agent_openai.name}' created (using OpenAI).")

# Create the Brand Marketer Agent - Using OpenAI for now

brand_marketer_prompt = """You are the Brand Marketer for the shoe brand. Brainstorm creative, specific campaign ideas (digital, content, experiences).
Focus on tactics and details. Suggest KPIs for your ideas."""

brand_marketer_agent_openai = autogen.ConversableAgent(
    name = "Brand_Marketer_OpenAI",
    system_message = brand_marketer_prompt,
    llm_config = llm_config_openai,  # Assign the same OpenAI config
    human_input_mode = "NEVER")

print(f"Agent '{brand_marketer_agent_openai.name}' created (using OpenAI).")# Create the Brand Marketer Agent - Using OpenAI for now

brand_marketer_prompt = """You are the Brand Marketer for the shoe brand. Brainstorm creative, specific campaign ideas (digital, content, experiences).
Focus on tactics and details. Suggest KPIs for your ideas."""

# Create the Social_Media_Strategist - Using OpenAI for now

social_media_strategist_prompt = """You are the Social Media Strategist for the shoe brand. You play a key role
 in launching our coordinated social media marketing campaign.
  Create a social media strategy, posts and engagement strategies. Work with Brand Marketer and CMO"""

social_media_strategist_agent_openai = autogen.ConversableAgent(
    name = "Social_Media_Strategist_OpenAI",
    system_message = social_media_strategist_prompt,
    llm_config = llm_config_openai,  # Assign the same OpenAI config
    human_input_mode = "NEVER")

print(f"Agent '{social_media_strategist_agent_openai.name}' created (using OpenAI).")