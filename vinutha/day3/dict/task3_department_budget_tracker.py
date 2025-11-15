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
# 6. Display total company budget (sum of all budgets

#code

# Create a dictionary of departments
# Each department has a nested dictionary with 'manager' and 'budget'
departments = {
    "HR": {"manager": "Neha", "budget": 25},
    "IT": {"manager": "Arjun", "budget": 50},
    "Finance": {"manager": "Fatima", "budget": 40}
}

# Add a new department "Operations" with its manager and budget
departments.update({"Operations": {"manager": "Vikram", "budget": 35}})

# Update the budget of the Finance department
departments["Finance"]["budget"] = 45

# Print the manager of the IT department
print("IT Manager:", departments["IT"]["manager"])

# Loop through all departments and print their details
for dept, info in departments.items():
    print(f"{dept} | Manager: {info['manager']} | Budget: {info['budget']} Lakhs")

# Calculate the total company budget by summing all department budgets
total = sum(info["budget"] for info in departments.values())

# Print the total company budget
print("Total Company Budget:", total, "Lakhs")

#output

# PS C:\Users\303379\day3_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day3_training/task3_Department_Budget_Tracker.py
# IT Manager: Arjun
# HR | Manager: Neha | Budget: 25 Lakhs
# IT | Manager: Arjun | Budget: 50 Lakhs
# Finance | Manager: Fatima | Budget: 45 Lakhs
# Operations | Manager: Vikram | Budget: 35 Lakhs
# Total Company Budget: 155 Lakhs
# PS C:\Users\303379\day3_training> 
