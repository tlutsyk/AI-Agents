"""
This is the main function that runs the handoff chain end-to-end with a sample query.
"""
import asyncio

from agents import Runner, SQLiteSession

from handoffs.writer import planner_with_handoff

session = SQLiteSession("run_handoffs_demo");

async def run_handoffs_demo(user_query: str):
    print(f"## 🕵️‍♀️ User Query\n{user_query}")  # Display the user query

    # Start the chain at the Planner; it will handoff to Writer
    run_res = await Runner.run(planner_with_handoff, user_query, session = session)
    print("---")  # Separator for output

    # Check if the final output is from the Verifier and display the result
    report = run_res.final_output

    # Display (This part is correct)
    print("---")
    print(f"### 🔎 Executive Summary\n{report.short_summary}")
    print("\n\n-----------------\n\n")
    print(f"### 📄 Full Report\n{report.markdown_report}")
    print("\n\n-----------------\n\n")
    return run_res

async def main():
    handoff_result = await run_handoffs_demo("Compare the weather in Prague and in Kyiv in Summer")

asyncio.run(main())

print("The end")
