from langchain_groq import ChatGroq

from langchain.agents import create_agent

from agent.tools import tools


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


agent_executor = create_agent(

    model=llm,

    tools=tools,

    system_prompt=
#     """
# You are an AI Travel Planner.

# Use tools whenever required.

# Provide:

# - Weather
# - Budget
# - Places
# - Travel tips

# Keep answer short.
# """


"""
You are an AI Travel Planner.

Always use tools before answering.

Generate output in this exact format:

Trip Summary:
Short trip plan

Weather:
Current temperature and condition

Budget:
Estimated trip budget

Places:
Recommended places

Travel Tips:
Helpful travel tips

Never skip Weather, Budget or Places.
"""
)