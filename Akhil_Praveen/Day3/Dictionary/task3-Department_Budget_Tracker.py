# Department_Budget_Tracker

departments = {
 "HR": {"manager": "Neha", "budget": 25},
 "IT": {"manager": "Arjun", "budget": 50},
 "Finance": {"manager": "Fatima", "budget": 40}
}
departments["Operations"]= {"manager": "Vikram", "budget": 35}
departments["Finance"]["budget"]=45
print(departments["IT"]["manager"])
sum=0
for i in departments:
    print(f"Department: {i} | Manager: {departments[i]["manager"]} | Budget: {departments[i]["budget"]} Lakhs")
    sum+=departments[i]["budget"]
print("Sum of all budgets: ",sum)

# Arjun
# Department: HR | Manager: Neha | Budget: 25 Lakhs
# Department: IT | Manager: Arjun | Budget: 50 Lakhs
# Department: Finance | Manager: Fatima | Budget: 45 Lakhs
# Department: Operations | Manager: Vikram | Budget: 35 Lakhs
# Sum of all budgets:  155