from agents import AgentHooks

class PrintHooks(AgentHooks):
    @staticmethod
    async def on_start(context, agent):
        print(f"🚀 {agent.name} started")

    @staticmethod
    async def on_end(context, agent, output):
        print(f"✅ {agent.name} finished")

print_hooks = PrintHooks();
