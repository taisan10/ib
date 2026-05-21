from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

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


query = "Tell me best places in Goa"


docs = retriever.invoke(
    query
)


context = "\n".join(
    [doc.page_content for doc in docs]
)


prompt = f"""
# Answer ONLY from context.

Context:
{context}

Question:
{query}
"""


response = llm.invoke(
    prompt
)


print(response.content)