from database.mongodb import chat_collection


async def save_message(
    session_id,
    role,
    message
):
    await chat_collection.insert_one({
        "session_id": session_id,
        "role": role,
        "message": message
    })


async def get_history(
    session_id
):

    cursor = chat_collection.find(
        {
            "session_id": session_id
        }
    )

    history = []

    async for chat in cursor:

        history.append({
            "role": chat["role"],
            "message": chat["message"]
        })

    return "\n".join(history)