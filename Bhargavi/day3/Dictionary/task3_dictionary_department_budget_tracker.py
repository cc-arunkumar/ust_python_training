# Department Budget Tracker(Nested Dictionary)

# Task 3: Department Budget Tracker
# (Nested Dictionary)

# Scenario:
# The Finance team maintains a yearly budget tracker for each department.
# Dictionary Tasks 2

# Instructions:
# 1. Create a nested dictionary:
# departments = {
#  "HR": {"manager": "Neha", "budget": 25},
#  "IT": {"manager": "Arjun", "budget": 50},
#  "Finance": {"manager": "Fatima", "budget": 40}
# }
# 2. Add "Operations": {"manager": "Vikram", "budget": 35} .
# 3. Update Finance budget → 45 .
# 4. Print IT’s manager name.
# 5. Print each department:
# Department: HR | Manager: Neha | Budget: 25 Lakhs
# 6. Display total company budget (sum of all budgets).

# Dictionary of departments with manager and budget
departments = {
    "HR": {"manager": "Neha", "budget": 25},
    "IT": {"manager": "Arjun", "budget": 50},
    "Finance": {"manager": "Fatima", "budget": 40}
}

# Add a new department
departments["Operations"] = {"manager": "Vikram", "budget": 35}

# Update Finance department budget
departments["Finance"]["budget"] = 45

# Print manager of IT department
print("IT Manager:", departments["IT"]["manager"])

# Loop through all departments and print details
for dept, info in departments.items():
    print(f"Department: {dept} | Manager: {info['manager']} | Budget: {info['budget']} Lakhs")

# Calculate total company budget
total_budget = sum(info["budget"] for info in departments.values())
print("Total Company Budget:", total_budget, "Lakhs")


# Output:
# IT Manager: Arjun
# Department: HR | Manager: Neha | Budget: 25 Lakhs
# Department: IT | Manager: Arjun | Budget: 50 Lakhs
# Department: Finance | Manager: Fatima | Budget: 45 Lakhs
# Department: Operations | Manager: Vikram | Budget: 35 Lakhs
# Total Company Budget: 155 Lakhs
