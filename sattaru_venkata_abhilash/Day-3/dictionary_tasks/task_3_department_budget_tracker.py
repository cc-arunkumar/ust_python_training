# Task 3: Department Budget Tracker
# Scenario:
# The Finance team maintains a yearly budget tracker for each department.
# Instructions:
# 1. Create a nested dictionary.
# 2. Add a new department.
# 3. Update Finance budget.
# 4. Print IT’s manager name.
# 5. Display all department details.
# 6. Show total company budget.

departments = {
    "HR": {"manager": "Neha", "budget": 25},
    "IT": {"manager": "Arjun", "budget": 50},
    "Finance": {"manager": "Fatima", "budget": 40}
}

# Step 1: Add a new department
departments["Operations"] = {"manager": "Vikram", "budget": 35}

# Step 2: Update Finance budget
departments["Finance"]["budget"] = 45

# Step 3: Print IT Manager
print("IT Manager:", departments["IT"]["manager"])

# Step 4: Print all departments
for dept, val in departments.items():
    print(f"Department: {dept} | Manager: {val['manager']} | Budget: {val['budget']} Lakhs")

# Step 5: Calculate total company budget
total_budget = sum(info["budget"] for info in departments.values())
print("\nTotal Company Budget:", total_budget, "Lakhs")

# Step 6: Print full dictionary
print("\nDepartments Data:", departments)


# Sample Output:
# IT Manager: Arjun
# Department: HR | Manager: Neha | Budget: 25 Lakhs
# Department: IT | Manager: Arjun | Budget: 50 Lakhs
# Department: Finance | Manager: Fatima | Budget: 45 Lakhs
# Department: Operations | Manager: Vikram | Budget: 35 Lakhs
#
# Total Company Budget: 155 Lakhs
#
# Departments Data: {'HR': {'manager': 'Neha', 'budget': 25}, 'IT': {'manager': 'Arjun', 'budget': 50},
#                    'Finance': {'manager': 'Fatima', 'budget': 45}, 'Operations': {'manager': 'Vikram', 'budget': 35}}
