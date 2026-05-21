from database.chat_db import (
    conn,
    cursor
)



def save_message(
    session_id:str,
    role:str,
    message:str
):


    cursor.execute(

"""
INSERT INTO chats(
session_id,
role,
message
)

VALUES(?,?,?)

""",

(
session_id,
role,
message
)

)


    conn.commit()



def get_history(
    session_id:str
):


    cursor.execute(

"""
SELECT role,message

FROM chats

WHERE session_id=?

""",

(session_id,)

)


    rows=cursor.fetchall()


    history=[]


    for role,message in rows:

        history.append(

            f"{role}:{message}"

        )


    return "\n".join(
        history
    )