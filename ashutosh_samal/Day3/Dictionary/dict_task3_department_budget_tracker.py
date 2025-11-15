#Task 3: Department Budget Tracker

# Dictionary representing departments with their respective manager names and budget
departments = {
    "HR": {"manager": "Neha", "budget": 25},
    "IT": {"manager": "Arjun", "budget": 50},
    "Finance": {"manager": "Fatima", "budget": 40}
}

# Adding a new department "Operations" with manager and budget information
departments["Operations"] = {"manager": "Vikram", "budget": 35}

# Updating the budget of the "Finance" department
departments["Finance"]["budget"] = 45

# Accessing and printing the name of the manager of the "IT" department
print("IT's manager name:", departments["IT"]["manager"])

# Variable to store the sum of all department budgets
total_budget = 0

# Looping through each department to print the details and calculate the total budget
for dept, info in departments.items():
    print(f"Department: {dept} | Manager: {info['manager']} | Budget: {info['budget']}")
    total_budget += info['budget']  # Adding each department's budget to the total

# Printing the total company budget
print("Total company budget: ", total_budget)


#Sample Execution
# IT's manager name: Arjun
# Department: HR | Manager: Neha | Budget: 25
# Department: IT | Manager: Arjun | Budget: 50
# Department: Finance | Manager: Fatima | Budget: 45
# Department: Operations | Manager: Vikram | Budget: 35
# Total company budget:  155