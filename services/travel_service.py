from tools.weather_tool import get_weather
from tools.budget_tool import estimate_budget
from tools.place_tool import search_places

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