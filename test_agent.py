from agent.agent_builder import (
    agent_executor
)

result = agent_executor.invoke(
    {
        "messages":[
            (
                "human",
                "Plan Goa trip for 3 days"
            )
        ]
    }
)

print("\nAI RESPONSE:\n")

print(
    result["messages"][-1].content
)