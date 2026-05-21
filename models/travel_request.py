from pydantic import BaseModel


class TravelRequest(BaseModel):

    session_id:str

    city:str

    days:int