import os 
from dotenv import load_dotenv

from langchain.tools import tool

from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_community.vectorstores import Chroma


load_dotenv()


embeddings = GoogleGenerativeAIEmbeddings( model="models/gemini-embedding-001", google_api_key=os.getenv("GOOGLE_API_KEY") )

db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

retriever = db.as_retriever(
    search_kwargs={"k": 1}
)


@tool
def search_places(city: str) -> str:

    """
    Travel guide information
    """



    docs = retriever.invoke(
        f"best places in {city}"
    )

    result = "\n".join(
        [doc.page_content for doc in docs]
    )

    return result