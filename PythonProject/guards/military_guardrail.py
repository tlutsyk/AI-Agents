from typing import Union, List

from agents import TResponseInputItem
from agents import input_guardrail, Runner, RunContextWrapper, Agent, GuardrailFunctionOutput
from pydantic import BaseModel


class MilitaryTopicOutput(BaseModel):
    is_military: bool
    reasoning: str

military_guardrail_agent = Agent(name = "Guardrail check",
                                 instructions = "Check if the user is asking about military topics, or anything related to military. If so, set is_military to true and explain why in reasoning.",
                                 output_type = MilitaryTopicOutput)

@input_guardrail
async def military_guardrail(ctx: RunContextWrapper[None], agent: Agent, input: Union[str, List[TResponseInputItem]]) -> GuardrailFunctionOutput:

    # Use the guardrail agent to classify the input.
    result = await Runner.run(military_guardrail_agent, input, context = ctx.context)

    # output_info: stores the full structured output (is_military + reasoning).
    # tripwire_triggered: this is the key flag. If is_military == True, then the guardrail has been triggered.
    return GuardrailFunctionOutput(output_info = result.final_output,
                                   tripwire_triggered = result.final_output.is_military)
