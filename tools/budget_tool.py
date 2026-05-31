# from langchain.tools import tool


# @tool
# def estimate_budget(
#     city:str,
#     days:int
# )->str:

#     """
#     Estimate travel budget
#     """

#     budget_data = {

#         "Goa":3000,

#         "Jaipur":2500,

#         "Delhi":3500
#     }

#     if city not in budget_data:

#         return "City budget data not available"


#     total = budget_data[city]*days


#     return (
#         f"Estimated budget for "
#         f"{days} days in {city}: ₹{total}"
#     )



from langchain.tools import tool


@tool
def estimate_budget(input: str) -> str:
    """
    Estimate travel budget.
    Input format: "city,days"
    Example: "Goa,3"
    """

    try:
        city, days = input.split(",")
        days = int(days.strip())
        city = city.strip()
    except:
        return "Invalid input format. Use: city,days (e.g. Goa,3)"

    budget_data = {
        "Goa": 3000,
        "Jaipur": 2500,
        "Delhi": 3500
    }

    if city not in budget_data:
        return "City budget data not available"

    total = budget_data[city] * days

    return f"Estimated budget for {days} days in {city}: ₹{total}"