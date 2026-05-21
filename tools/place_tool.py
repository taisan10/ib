# from langchain.tools import tool

# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.vectorstores import FAISS


# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )


# db = FAISS.load_local(
#     "faiss_index",
#     embeddings,
#     allow_dangerous_deserialization=True
# )


# retriever = db.as_retriever(
#     search_kwargs={"k":1}
# )


# @tool
# def search_places(city:str)->str:
#     """
#     Search travel places from vector database
#     """

#     docs = retriever.invoke(
#         f"best places in {city}"
#     )

#     result = "\n".join(
#         [doc.page_content for doc in docs]
#     )

#     return result
from langchain.tools import tool

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# IMPORTANT
from rag.data.travel_data import travel_data


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