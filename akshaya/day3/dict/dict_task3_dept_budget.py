# Task 3: Department Budget Tracker

departments = {
    "HR": {"manager": "Neha", "budget": 25},
    "IT": {"manager": "Arjun", "budget": 50},
    "Finance": {"manager": "Fatima", "budget": 40}
}

departments["Operations"] = {"manager": "Vikram", "budget": 35}

departments["Finance"]["budget"] = 45

print("IT Manager:", departments["IT"]["manager"])

print("\nDepartment Details:")
for dept, info in departments.items():
    print(f"Department: {dept} | Manager: {info['manager']} | Budget: {info['budget']} Lakhs")

total_budget = sum(info["budget"] for info in departments.values())
print(f"\nTotal Company Budget: {total_budget} Lakhs")

#sample output
# IT Manager: Arjun

# Department Details:
# Department: HR | Manager: Neha | Budget: 25 Lakhs
# Department: IT | Manager: Arjun | Budget: 50 Lakhs
# Department: Finance | Manager: Fatima | Budget: 45 Lakhs
# Department: Operations | Manager: Vikram | Budget: 35 Lakhs

# Total Company Budget: 155 Lakhs
