#Task 3: Department Budget Tracker(Nested Dictionary)

#Code
departments = {
 "HR": {"manager": "Neha", "budget": 25},
 "IT": {"manager": "Arjun", "budget": 50},
 "Finance": {"manager": "Fatima", "budget": 40}
}

departments["Operations"]={"manager":"Neha","budget":25}
departments["Finance"]= {"budget":45}
print("IT Manager name is : ",departments["IT"]["manager"])
for dept , info in departments.items():
  manager = info.get("manager", "N/A")
  budget = info.get("budget",0)
  print(f"Department : {dept} | Manager : {manager} | Budget : {budget} lakhs")
total_budget = sum(info.get('budget',0) for info in departments.values())
print("The total budget is : ",total_budget)

#Output
# IT Manager name is :  Arjun
# Department : HR | Manager : Neha | Budget : 25 lakhs
# Department : IT | Manager : Arjun | Budget : 50 lakhs
# Department : Finance | Manager : N/A | Budget : 45 lakhs
# Department : Operations | Manager : Neha | Budget : 25 lakhs
# The total budget is :  145
