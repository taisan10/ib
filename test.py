# test.py
import asyncio
import certifi
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

async def test():
    client = AsyncIOMotorClient(
        os.getenv("MONGODB_URI"),
        tlsCAFile=certifi.where()
    )
    try:
        await client.admin.command("ping")
        print("✅ MongoDB connected!")
    except Exception as e:
        print(f"❌ Error: {e}")

asyncio.run(test())