# Define departments dictionary with manager and budget
departments = {
    "HR": {"manager": "Neha", "budget": 25},
    "IT": {"manager": "Arjun", "budget": 50},
    "Finance": {"manager": "Fatima", "budget": 40}
}

# Add a new department
departments["Operations"] = {"manager": "Vikram", "budget": 35}

# Update Finance department budget
departments["Finance"]["budget"] = 45

# Print IT manager
print("IT Manager:", departments["IT"]["manager"])

# Print all department details
for dept, info in departments.items():
    print(f"Department: {dept} | Manager: {info['manager']} | Budget: {info['budget']} Lakhs")

# Calculate total budget across all departments
total_budget = sum(info["budget"] for info in departments.values())
print("Total Budget:", total_budget, "Lakhs")

# -------------------------
# Expected Output:
# IT Manager: Arjun
# Department: HR | Manager: Neha | Budget: 25 Lakhs
# Department: IT | Manager: Arjun | Budget: 50 Lakhs
# Department: Finance | Manager: Fatima | Budget: 45 Lakhs
# Department: Operations | Manager: Vikram | Budget: 35 Lakhs
# Total Budget: 155 Lakhs