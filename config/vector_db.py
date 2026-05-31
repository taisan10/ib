from dotenv import load_dotenv
import os

from pinecone import Pinecone
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)

index_name = os.getenv(
    "PINECONE_INDEX_NAME"
)

if not index_name:
    raise ValueError("PINECONE_INDEX_NAME not found")
   

vector_store = PineconeVectorStore(
    index_name=index_name,
    embedding=embeddings
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 1}
)