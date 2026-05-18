from agents import RunResult

async def extract_summary(run_result: RunResult) -> str:
    """Extracts the 'summary' field from the final_output of an agent run."""
    return run_result.final_output.summary