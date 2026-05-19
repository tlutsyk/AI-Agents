from planner_agents import cmo_agent_openai, brand_marketer_agent_openai

from helpers.print_markdown import print_markdown

initial_task_message = """
    Context: We're launching a new sustainable shoe line and need campaign ideas
    Instruction: Brainstorm a campaign concept with specific elements
    Input: Our sustainable, futuristic shoe brand needs marketing direction
    Output: A concise campaign concept with the following structure:
    Brand Marketer, let's brainstorm initial campaign ideas for our new sustainable shoe line.
    Give me a distinct campaign concept. Outline: core idea, target audience, primary channels, and 1-2 KPIs. Keep it concise. Try to arrive at a final answer in 2-3 turns.
    """

print("--- Starting Agent Conversation (OpenAI Only) ---")
print("Chief Marketing Officer (OpenAI) initiating chat with Brand Marketer (OpenAI). Max Turns = 4")
print("--------------------------------------------------")

# Chief Marketing Officer (OpenAI) initiates the chat with Brand Marketer (OpenAI)
chat_result_openai_only = cmo_agent_openai.initiate_chat(
    recipient = brand_marketer_agent_openai, message = initial_task_message, max_turns = 4
)

print("--------------------------------------------------")
print("--- Conversation Ended (OpenAI Only) ---")

def print_chat_history(chat_result):
    """Any chat result object has a chat_history attribute that contains the conversation history.
    This function prints the conversation history in a readable format.
    """
    for i in chat_result.chat_history:
        print_markdown(i['name'])
        print("_"*100)
        print_markdown(i['content'])
        print("_"*100)

print_chat_history(chat_result_openai_only)