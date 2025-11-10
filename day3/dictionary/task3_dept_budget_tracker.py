departments = {
    "HR": {"manager": "Neha", "budget": 25},
    "IT": {"manager": "Arjun", "budget": 50},
    "Finance": {"manager": "Fatima", "budget": 40}
}

departments["Operations"] = {"manager": "Vikram", "budget": 35}


departments["Finance"]["budget"] = 45


print("IT Manager:", departments["IT"]["manager"])


for dept, info in departments.items():
    print(f"Department: {dept} | Manager: {info['manager']} | Budget: {info['budget']} Lakhs")

total_budget = sum(info["budget"] for info in departments.values())
