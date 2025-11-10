#Task 3: Department Budget Tracker

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

new_val = dict(manager="Vikram",budget=35)
departments["Operations"]=new_val
finance_dict = departments["Finance"]
finance_dict["budget"]=45

print("IT Manager Name is:",departments["IT"]['manager'])
#print("IT Manager Name is:",it_dict["manager"])

total_budget = 0
for dept in departments.items():
    total_budget += dept[1].get("budget")
    print(f"Department: {dept[0]} | Manager: {dept[1].get("manager")} | Budget: {dept[1].get("budget")} Lakhs")

print("Total Budget: ",total_budget," Lakhs")


#Sample Output
# IT Manager Name is: Arjun
# Department: HR | Manager: Neha | Budget: 25 Lakhs
# Department: IT | Manager: Arjun | Budget: 50 Lakhs
# Department: Finance | Manager: Fatima | Budget: 45 Lakhs
# Department: Operations | Manager: Vikram | Budget: 35 Lakhs
# Total Budget:  155  Lakhs