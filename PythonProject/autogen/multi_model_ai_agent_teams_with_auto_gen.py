# Note that this demo illustrates the potential benefit of using multiple models in agent-based systems, where each model's strengths can be leveraged for specific roles in the conversation.
# Nott that The Gemini and OpenAI combination created a more balanced conversation
# Gemini's conciseness as CMO complemented OpenAI's creative detail as Marketer
# The conversation flow was more efficient with clearer role differentiation
# Demonstrated how different models can be strategically assigned to roles that match their strengths
from initial_chat import print_chat_history, initial_task_message
from cmo_agent_gemini import cmo_agent_gemini, brand_marketer_agent_openai_mixed

print("--- Starting Agent Conversation (Multi-Model: Gemini + OpenAI) ---")
print("Chief Marketing Officer (Gemini) initiating chat with Brand Marketer (OpenAI). Max Turns = 4")
print("------------------------------------------------------------------")

# Chief Marketing Officer (Gemini) initiates the chat with the Brand Marketer (OpenAI)
chat_result_multi_model = cmo_agent_gemini.initiate_chat(
    recipient = brand_marketer_agent_openai_mixed,  # Target the OpenAI marketer
    message = initial_task_message,
    max_turns = 4)

print("------------------------------------------------------------------")
print("--- Conversation Ended (Multi-Model) ---")

print_chat_history(chat_result_multi_model)