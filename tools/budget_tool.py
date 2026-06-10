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
    Input format: city,days

    Example:
    Jaipur,3
    Goa,5
    """

    try:
        city, days = input.split(",")
        city = city.strip().title()
        days = int(days.strip())
    except:
        return "Invalid input format. Use: city,days"

    # Average budget per day (Hotel + Food + Local Travel)
    budget_data = {
        # Rajasthan
        "Jaipur": 2500,
        "Udaipur": 3000,
        "Jaisalmer": 2800,

        # Goa
        "Goa": 3500,

        # Delhi
        "Delhi": 3000,

        # Maharashtra
        "Mumbai": 4500,
        "Pune": 2500,

        # Karnataka
        "Bengaluru": 3000,
        "Mysuru": 2200,
        "Hampi": 1800,

        # Gujarat
        "Ahmedabad": 2500,

        # Punjab
        "Amritsar": 2200,

        # Haryana
        "Haryana": 2000,

        # Chandigarh
        "Chandigarh": 2500,

        # Himachal
        "Shimla": 2800,

        # Uttarakhand
        "Dehradun": 2500,

        # Uttar Pradesh
        "Uttar Pradesh": 2200,

        # Bihar
        "Bihar": 1800,

        # Jharkhand
        "Jharkhand": 1800,

        # Chhattisgarh
        "Chhattisgarh": 1800,

        # Odisha
        "Odisha": 2200,

        # West Bengal
        "West Bengal": 2500,

        # Sikkim
        "Sikkim": 3200,

        # Assam
        "Assam": 2500,

        # Arunachal Pradesh
        "Arunachal Pradesh": 3500,

        # Meghalaya
        "Meghalaya": 3000,

        # Manipur
        "Manipur": 2500,

        # Mizoram
        "Mizoram": 2500,

        # Nagaland
        "Nagaland": 2800,

        # Tripura
        "Tripura": 2200,

        # Jammu & Kashmir
        "Jammu And Kashmir": 3500,

        # Ladakh
        "Ladakh": 4500,

        # Puducherry
        "Puducherry": 2800,

        # Islands
        "Andaman And Nicobar Islands": 5000,
        "Lakshadweep": 6000,

        # Daman & Diu
        "Dadra And Nagar Haveli And Daman And Diu": 2500,
    }

    if city not in budget_data:
        available = ", ".join(sorted(budget_data.keys()))
        return (
            f"Budget data not available for '{city}'.\n\n"
            f"Available locations:\n{available}"
        )

    per_day_budget = budget_data[city]
    total_budget = per_day_budget * days

    return (
        f"📍 Location: {city}\n"
        f"🗓 Days: {days}\n"
        f"💰 Budget Per Day: ₹{per_day_budget:,}\n"
        f"💵 Estimated Total Budget: ₹{total_budget:,}"
    )