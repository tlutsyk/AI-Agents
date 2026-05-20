# Now we are ready to compile and execute the graph
# After defining your graph, you need to compile it to create an executable workflow
# Invoke it with an initial state to run the entire process
from helpers.print_markdown import print_markdown
from langgraph_project.simple_workflow import workflow

# Example text to summarize
sample_text = """
    Electric cars work by using electricity stored in a battery pack to power an electric motor, which drives the wheels. 
    Unlike gasoline-powered vehicles that rely on internal combustion engines, electric vehicles (EVS) use electric motors that are more efficient and produce zero emissions during operation. 
    When you press the accelerator, the battery sends power to the motor, which instantly provides torque to move the car. 
    The battery is recharged by plugging the car into an external power source, such as a home charger or public charging station. 
    Some electric cars also feature regenerative braking, which captures energy during braking and feeds it back into the battery to improve efficiency.
    """

# Let's compile the graph
graph = workflow.compile()

# Set up the initial state with the input text
initial_state = {
    "input_text": sample_text,
    "summary": "",
    "translation": "",
    "sentiment_marker": "",
}

# Run the graph
result = graph.invoke(initial_state)

# Get the summary from the result
summary = result["summary"]
print_markdown(summary)

# Print the translation
translation = result["translation"]
print_markdown(translation)

# Print the sentiment_marker
sentiment_marker = result["sentiment_marker"]
print_markdown(sentiment_marker)
