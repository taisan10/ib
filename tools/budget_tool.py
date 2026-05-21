from langchain.tools import tool


@tool
def estimate_budget(
    city:str,
    days:int
)->str:

    """
    Estimate travel budget
    """

    budget_data = {

        "Goa":3000,

        "Jaipur":2500,

        "Delhi":3500
    }

    if city not in budget_data:

        return "City budget data not available"


    total = budget_data[city]*days


    return (
        f"Estimated budget for "
        f"{days} days in {city}: ₹{total}"
    )