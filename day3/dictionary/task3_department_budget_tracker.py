# Task 3: Department Budget Tracker
# (Nested Dictionary)
# Scenario:
# The Finance team maintains a yearly budget tracker for each department.

departments = {
 "HR": {"manager": "Neha", "budget": 25},
 "IT": {"manager": "Arjun", "budget": 50},
 "Finance": {"manager": "Fatima", "budget": 40}
}

#add operations
departments["operations"] = {"manager": "Vikram", "budget": 35}
# print(departments)

#update finance budget
departments["Finance"] = {"manager": "Fatima","budget":45}
# print(departments)

# print(departments["IT"]["manager"])

# task 4 rint each department:

for dep,info in departments.items():
    print(f"Department :{dep} | manager:{info['manager']} | budget:{info['budget']} lakhs")

    total_budget = sum(info["budget"] for info in departments.values())

# sample output:
# Department :IT | manager:Arjun | budget:50 lakhs
# Department :Finance | manager:Fatima | budget:45 lakhs
# Department :operations | manager:Vikram | budget:35 lakhs