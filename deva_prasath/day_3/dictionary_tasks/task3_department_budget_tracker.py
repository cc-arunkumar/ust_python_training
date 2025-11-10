# department_budget_tracker
# The Finance team maintains a yearly budget tracker for each department.

departments = {
 "HR": {"manager": "Neha", "budget": 25},
 "IT": {"manager": "Arjun", "budget": 50},
 "Finance": {"manager": "Fatima", "budget": 40}
}
departments["Operations"]= {"manager": "Vikram", "budget": 35}
sumi=0
departments["Finance"]["budget"] = 45
print("Updated Finance Budget: ",departments)
print("IT manager name: ",departments["IT"]["manager"])
for key,val in departments.items():
    print(f"Department: {key} | Manager: {departments[key]["manager"]} | Budget :{departments[key]["budget"]}Lakhs")
for  key,val in departments.items():
    sumi+=departments[key]["budget"]
print("Total Company Budget:",sumi)




#Sample output

# Updated Finance Budget:  {'HR': {'manager': 'Neha', 'budget': 25}, 'IT': {'manager': 'Arjun', 'budget': 50}, 'Finance': {'manager': 'Fatima', 'budget': 45}, 'Operations': {'manager': 'Vikram', 'budget': 35}}
# IT manager name:  Arjun
# Department: HR | Manager: Neha | Budget :25Lakhs
# Department: IT | Manager: Arjun | Budget :50Lakhs
# Department: Finance | Manager: Fatima | Budget :45Lakhs
# Department: Operations | Manager: Vikram | Budget :35Lakhs
# Total Company Budget: 155