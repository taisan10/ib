from fastapi import FastAPI
from dotenv import load_dotenv

from langchain_groq import ChatGroq

from services.travel_service import create_context

from models.travel_request import TravelRequest
from database.chat_db import save_message, get_history
from fastapi.middleware.cors import CORSMiddleware

from agent.agent_builder import (
    agent_executor
)

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


@app.get("/")
def home():
    return {"status": "running"}


@app.post("/travel")
async def travel(         
    data: TravelRequest
):

    context = create_context(
        city=data.city,
        days=data.days
    )

    history = await get_history(  
        data.session_id
    )

    result = agent_executor.invoke(
        {
            "messages": [
                (
                    "human",
                    f"""
Plan a {data.days}-day trip for {data.city}.

Mandatory format:

Trip Summary:
Weather:
Budget:
Places:
Travel Tips:

Always use tool information.
Never skip Weather, Budget or Places.
"""
                )
            ]
        }
    )

    response = result["messages"][-1].content

    await save_message(          
        data.session_id,
        "Human",
        f"{data.city} for {data.days} days"
    )

    await save_message(           
        data.session_id,
        "AI",
        response
    )

    return {
        "answer": response,
        "city": data.city
    }

@app.get("/debug")
async def debug():
    import os
    return {
        "db_name": os.getenv("DATABASE_NAME"),
        "mongo_uri": os.getenv("MONGODB_URI")[:20]  # sirf starting dikhega
    }