from dotenv import load_dotenv
from pathlib import Path

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.documents import Document

import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

# travel_data.txt read
with open(
    BASE_DIR / "data" / "travel_data.txt",
    "r",
    encoding="utf-8"
) as f:
    data = f.read()

# city blocks split
cities = data.split(
    "=================================================="
)

documents = []

for city_data in cities:

    city_data = city_data.strip()

    if city_data:

        # City name extract
        city_name = "Unknown"

        lines = city_data.split("\n")

        for line in lines:

            if line.startswith("City:"):

                city_name = (
                    line.replace("City:", "")
                    .strip()
                )

                break

        documents.append(

            Document(
                page_content=city_data,
                metadata={
                    "city": city_name
                }
            )

        )

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=os.getenv(
        "GOOGLE_API_KEY"
    )
)

vector_store = PineconeVectorStore(
    index_name=os.getenv(
        "PINECONE_INDEX_NAME"
    ),
    embedding=embeddings
)

# upload documents
vector_store.add_documents(
    documents
)

print(
    f"{len(documents)} documents uploaded successfully"
)