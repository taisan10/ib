
from langchain.tools import tool

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
import os
# IMPORTANT
from rag.data.travel_data import travel_data


embeddings = GoogleGenerativeAIEmbeddings( model="models/embedding-001", google_api_key=os.getenv("GOOGLE_API_KEY") )

db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(
    search_kwargs={"k":1}
)


@tool
def search_places(city:str)->str:

    """
    Travel guide information
    """

    data = travel_data.get(city)

    if data:

        return f"""
{city}

Best Season:
{data['season']}

Recommended Days:
{data['recommended_days']}

Places:
{chr(10).join(data['places'])}

Food:
{chr(10).join(data['food'])}

Travel Tips:
{chr(10).join(data['tips'])}
"""

    # fallback FAISS
    docs = retriever.invoke(
        f"best places in {city}"
    )

    result="\n".join(
        [doc.page_content for doc in docs]
    )

    return result