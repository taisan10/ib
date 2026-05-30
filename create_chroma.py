from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_community.vectorstores import Chroma

from langchain_core.documents import Document

from dotenv import load_dotenv
import os

load_dotenv()


docs = [

    Document(
        page_content="Jaipur is famous for Hawa Mahal and Amer Fort"
    ),

    Document(
        page_content="Goa is famous for beaches and nightlife"
    ),

    Document(
        page_content="Manali is famous for snow mountains and adventure sports"
    )

]

from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(  model="models/gemini-embedding-001", google_api_key=os.getenv("GOOGLE_API_KEY") )



db = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory="chroma_db"
)

print("Chroma DB Created")