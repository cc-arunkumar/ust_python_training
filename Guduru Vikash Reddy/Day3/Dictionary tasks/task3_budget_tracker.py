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

departments = {
    "HR": {"manager": "Neha", "budget": 25},
    "IT": {"manager": "Arjun", "budget": 50},
    "Finance": {"manager": "Fatima", "budget": 40}
}

departments["Operations"] = {"manager": "Vikram", "budget": 35}
departments["Finance"]["budget"] = 45

print("IT Manager:", departments["IT"]["manager"])

total_budget = 0
for name, info in departments.items():
    print("Department:", name, "| Manager:", info["manager"], "| Budget:", info["budget"], "Lakhs")
    total_budget += info["budget"]

print("Total Company Budget:", total_budget, "Lakhs")

# sampleoutput
# IT Manager: Arjun
# Department: HR | Manager: Neha | Budget: 25 Lakhs
# Department: IT | Manager: Arjun | Budget: 50 Lakhs
# Department: Finance | Manager: Fatima | Budget: 45 Lakhs
# Department: Operations | Manager: Vikram | Budget: 35 Lakhs
# Total Company Budget: 155 Lakhs
