# Create the User Proxy Agent (Represents You)
import autogen

from cmo_agent_gemini import cmo_agent_gemini, brand_marketer_agent_openai_mixed
from planner_agents import brand_marketer_agent_openai
from autogen_config import llm_config_openai

user_proxy_agent = autogen.UserProxyAgent(
    name="Human_User_Proxy",
    human_input_mode="ALWAYS",
    code_execution_config=False,
    max_consecutive_auto_reply=0,
)

cmo_agent_gemini.reset()  # Reset Gemini CMO
brand_marketer_agent_openai_mixed.reset()  # Reset OpenAI Marketer
user_proxy_agent.reset()

from autogen import GroupChat, GroupChatManager

print("groupchat")

# Create a GroupChat with multiple agents
# This sets up a collaborative chat environment where multiple agents can interact
groupchat = GroupChat(
    agents = [user_proxy_agent, brand_marketer_agent_openai],  # List of agents participating in the group chat
    messages = [ ],  # Initialize with empty message history
    max_round = 20,  # Optional: Limits how many conversation rounds can occur before terminating
)

print("group_manager")


# Create a manager for the group chat
# The GroupChatManager orchestrates the conversation flow between agents
# It determines which agent should speak next and handles the overall conversation logic
group_manager = GroupChatManager(groupchat = groupchat, llm_config = llm_config_openai)  # Uses OpenAI's LLM to manage the conversation

print("group_chat_result")


# User Proxy initiates the chat - Let's give a new task
group_chat_result = user_proxy_agent.initiate_chat(
    recipient = group_manager,
    message = "Hello team!!",
)

print("---------------------------------------------------------------------")
print("--- Conversation Ended (Human terminated or Max Turns) ---")