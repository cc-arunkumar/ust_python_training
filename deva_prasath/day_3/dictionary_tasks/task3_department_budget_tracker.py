# department_budget_tracker
# The Finance team maintains a yearly budget tracker for each department.
# Dictionary storing department information with manager and budget
departments = {
    "HR": {"manager": "Neha", "budget": 25},
    "IT": {"manager": "Arjun", "budget": 50},
    "Finance": {"manager": "Fatima", "budget": 40}
}

# Add a new department (Operations) with manager and budget
departments["Operations"] = {"manager": "Vikram", "budget": 35}

# Initialize a variable to calculate total budget
sumi = 0

# Update the budget for the Finance department
departments["Finance"]["budget"] = 45

# Print the updated Finance department budget
print("Updated Finance Budget: ", departments)

# Print the manager name for the IT department
print("IT manager name: ", departments["IT"]["manager"])

# Iterate through departments and print department details
for key, val in departments.items():
    print(f"Department: {key} | Manager: {departments[key]['manager']} | Budget: {departments[key]['budget']} Lakhs")

# Calculate the total company budget by summing individual department budgets
for key, val in departments.items():
    sumi += departments[key]["budget"]

# Print the total company budget
print("Total Company Budget:", sumi)





#Sample output

# Updated Finance Budget:  {'HR': {'manager': 'Neha', 'budget': 25}, 'IT': {'manager': 'Arjun', 'budget': 50}, 'Finance': {'manager': 'Fatima', 'budget': 45}, 'Operations': {'manager': 'Vikram', 'budget': 35}}
# IT manager name:  Arjun
# Department: HR | Manager: Neha | Budget :25Lakhs
# Department: IT | Manager: Arjun | Budget :50Lakhs
# Department: Finance | Manager: Fatima | Budget :45Lakhs
# Department: Operations | Manager: Vikram | Budget :35Lakhs
# Total Company Budget: 155