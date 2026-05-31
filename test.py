# from config.vector_db import retriever

# docs = retriever.invoke(
#     "best places in Gujarat"
# )

# for doc in docs:
#     print(doc.page_content)


from services.travel_service import create_context

print(
    create_context(
        city="Pune",
        days=4
    )
)