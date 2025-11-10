# TASK 3 Department Budget Tracker

departments = {
 "HR": {"manager": "Neha", "budget": 25},
 "IT": {"manager": "Arjun", "budget": 50},
 "Finance": {"manager": "Fatima", "budget": 40}
}

departments["Operations"]={"manager":"Vikram","budget":35}

for dept,val in departments.items():
    if dept == "Finance":
        val["budget"] = 45

print("IT Manager:", departments["IT"]["manager"])
print()

for dept, details in departments.items():
    print(f"Department: {dept} | Manager: {details['manager']} | Budget: {details['budget']} Lakhs")

print()

total_budget = sum(details["budget"] for details in departments.values())
print("Total Company Budget:", total_budget, "Lakhs")

# ---------------------------------------------------------------------------
# IT Manager: Arjun

# Department: HR | Manager: Neha | Budget: 25 Lakhs
# Department: IT | Manager: Arjun | Budget: 50 Lakhs
# Department: Finance | Manager: Fatima | Budget: 45 Lakhs
# Department: Operations | Manager: Vikram | Budget: 35 Lakhs

# Total Company Budget: 155 Lakhs


            






