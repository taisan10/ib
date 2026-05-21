from pydantic import BaseModel


class TravelPlan(BaseModel):

    city:str

    weather:str

    budget:int

    recommendation:str