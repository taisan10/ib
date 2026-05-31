# from dotenv import load_dotenv
# from langchain.tools import tool
# from config.vector_db import retriever

# load_dotenv()

# @tool
# def search_places(city: str) -> str:

#     """
#     Travel guide information
#     """

#     docs = retriever.invoke(
#         f"best places in {city}"
#     )

#     result = "\n".join(
#         [doc.page_content for doc in docs]
#     )

#     return result

from dotenv import load_dotenv
from langchain.tools import tool
from config.vector_db import retriever

load_dotenv()


@tool
def search_places(city: str) -> str:
    """
    Travel guide information
    """

    try:
        docs = retriever.invoke(
            f"best places in {city}"
        )

        if not docs:
            return "No places found for this city"

        result = "\n".join(
            doc.page_content for doc in docs
        )

        return result

    except Exception as e:
        return f"Error fetching places: {str(e)}"