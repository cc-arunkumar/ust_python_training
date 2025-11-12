# Task 3: Department Budget Tracker
# (Nested Dictionary)
# Scenario:
# The Finance team maintains a yearly budget tracker for each department.




# Step 1: Initialize the departments dictionary with nested dictionaries
departments = {
    "HR": {"manager": "Neha", "budget": 25},
    "IT": {"manager": "Arjun", "budget": 50},
    "Finance": {"manager": "Fatima", "budget": 40}
}

# Step 2: Add a new department dynamically
departments["Operations"] = {"manager": "Vikram", "budget": 35}

# Step 3: Print the updated departments dictionary
print(departments)

# Step 4: Update the budget for the Finance department
for item in departments:
    if item == "Finance":
        departments[item]["budget"] = 100

# Step 5: Print the departments dictionary after budget update
print(departments)

# Step 6: Print only the manager names for each department
print("Name of each department")
for item in departments:
  
    print(f"{departments[item]["manager"]}")

# Step 7: Print a formatted summary of each department
print("formatted summary of each department")
for item in departments:
    print("Department", item, "| Manager", departments[item]["manager"], "| Budget", departments[item]["budget"])

# =============sample-output======================
# {'HR': {'manager': 'Neha', 'budget': 25}, 'IT': {'manager': 'Arjun', 'budget': 50}, 'Finance': {'manager': 'Fatima', 'budget': 40}, 'Operations': {'manager': 'Vikram', 'budget': 35}}
# {'HR': {'manager': 'Neha', 'budget': 25}, 'IT': {'manager': 'Arjun', 'budget': 50}, 'Finance': {'manager': 'Fatima', 'budget': 100}, 'Operations': {'manager': 'Vikram', 'budget': 35}}
# Name of each department
# Neha
# Arjun
# Fatima
# Vikram
# formatted summary of each department
# Department HR | Manager Neha | Budget 25
# Department IT | Manager Arjun | Budget 50
# Department Finance | Manager Fatima | Budget 100
# Department Operations | Manager Vikram | Budget 35