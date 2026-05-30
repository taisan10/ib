from tools.weather_tool import get_weather
from tools.budget_tool import estimate_budget
from tools.place_tool import search_places
import os 
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_community.vectorstores import Chroma

embeddings = GoogleGenerativeAIEmbeddings( model="models/gemini-embedding-001", google_api_key=os.getenv("GOOGLE_API_KEY") )

db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

retriever = db.as_retriever(
    search_kwargs={"k":1}
)



def create_context(
    city:str,
    days:int
):


    weather = get_weather.invoke(
        city
    )


    budget = estimate_budget.invoke(
        {
            "city":city,
            "days":days
        }
    )


    places = search_places.invoke(
        city
    )


    final_context = f"""
Weather:
{weather}

Budget:
{budget}

Travel Data:
{places}
"""


    return final_context