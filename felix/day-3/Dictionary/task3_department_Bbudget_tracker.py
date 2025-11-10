# task3_Department_Budget_Tracker

departments = {
 "HR": {"manager": "Neha", "budget": 25},
 "IT": {"manager": "Arjun", "budget": 50},
 "Finance": {"manager": "Fatima", "budget": 40}
}

departments["Operations"] =  {"manager": "Vikram", "budget": 35}

departments["Finance"]["budget"] = 45

print(departments["IT"]["manager"])
total_budget = 0
for i in departments:
    print(f"Department: {i} | Manager: {departments[i]["manager"]} | Budget: {departments[i]["budget"]}")
    total_budget += departments[i]["budget"]

print("Total budget: ",total_budget)

# output

# Arjun
# Department: HR | Manager: Neha | Budget: 25
# Department: IT | Manager: Arjun | Budget: 50
# Department: Finance | Manager: Fatima | Budget: 45
# Department: Operations | Manager: Vikram | Budget: 35
# Total budget:  155