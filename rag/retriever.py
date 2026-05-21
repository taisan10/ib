from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


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


query = "Best beach in Goa"


results = retriever.invoke(
    query
)


for doc in results:

    print(doc.page_content)