"""
Task 3: Department Budget Tracker
(Nested Dictionary)

Scenario:
The Finance team maintains a yearly budget tracker for each department.

"""

# Dictionary storing department details as nested dictionaries
# Each department has a manager and a budget (in Lakhs)
departments={
"HR":{"manager":"Neha","budget":25},
"IT":{"manager":"Arjun","budget":50},
"Finance":{"manager":"Fatima","budget":40}
}

# Add a new department "Operations" with manager and budget
departments["Operations"]={"manager":"Vikram","budget":35}

# Update the budget for Finance department
departments["Finance"]["budget"]=45

# Print IT manager's name
print("IT Manager Name:",departments["IT"]["manager"])

# Print details of all departments
for dept,details in departments.items():
    print(f"Department: {dept} | Manager: {details['manager']} | Budget: {details['budget']} Lakhs")

# Calculate and print total company budget
total_budget=sum(d["budget"] for d in departments.values())
print("Total Company Budget:",total_budget,"Lakhs")


# sample output

"""
IT Manager Name: Arjun
Department: HR | Manager: Neha | Budget: 25 Lakhs
Department: IT | Manager: Arjun | Budget: 50 Lakhs
Department: Finance | Manager: Fatima | Budget: 45 Lakhs
Department: Operations | Manager: Vikram | Budget: 35 Lakhs
Total Company Budget: 155 Lakhs
"""
