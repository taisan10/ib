from tools.weather_tool import get_weather
from tools.budget_tool import estimate_budget
from tools.place_tool import search_places

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
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