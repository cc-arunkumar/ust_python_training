"""
Task 3: Department Budget Tracker
(Nested Dictionary)

Scenario:
The Finance team maintains a yearly budget tracker for each department.

"""

departments={
"HR":{"manager":"Neha","budget":25},
"IT":{"manager":"Arjun","budget":50},
"Finance":{"manager":"Fatima","budget":40}
}
departments["Operations"]={"manager":"Vikram","budget":35}

departments["Finance"]["budget"]=45
print("IT Manager Name:",departments["IT"]["manager"])

for dept,details in departments.items():
    print(f"Department: {dept} | Manager: {details['manager']} | Budget: {details['budget']} Lakhs")

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