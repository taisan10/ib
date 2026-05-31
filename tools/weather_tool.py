# import os
# import requests
# from dotenv import load_dotenv
# from langchain.tools import tool

# load_dotenv()


# @tool
# def get_weather(city: str) -> str:
#     """
#     Get current weather of a city
#     """

#     api_key = os.getenv(
#         "OPENWEATHER_API_KEY"
#     )
#     if not api_key:
#        return "OPENWEATHER_API_KEY not set in environment variables"

#     url = (
#         f"https://api.openweathermap.org/data/2.5/weather"
#         f"?q={city}"
#         f"&appid={api_key}"
#         f"&units=metric"
#     )

#     response = requests.get(url)
    
#     try:
#           data = response.json()
#     except:
#           return "Invalid response from weather API"


#     temp = data["main"]["temp"]

#     desc = data["weather"][0]["description"]

#     return (
#         f"{city} weather:\n"
#         f"Temperature: {temp}°C\n"
#         f"Condition: {desc}"
#     )



import os
import requests
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()


@tool
def get_weather(city: str) -> str:
    """
    Get current weather of a city
    """

    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        return "OPENWEATHER_API_KEY not set in environment variables"

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={api_key}"
        f"&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return "Weather data not found"

    try:
        data = response.json()
    except:
        return "Invalid response from weather API"

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    return (
        f"{city} weather:\n"
        f"Temperature: {temp}°C\n"
        f"Condition: {desc}"
    )