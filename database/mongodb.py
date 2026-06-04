from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import certifi
import os

load_dotenv()

client = AsyncIOMotorClient(
    os.getenv("MONGODB_URI"),
    tlsCAFile=certifi.where()
)

db = client[os.getenv("DATABASE_NAME")]
chat_collection = db["chats"]