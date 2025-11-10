# Task 3: Department Budget Tracker

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


departments["Operations"]={"manager": "Vikram", "budget": 35}

print(departments)

for dept, val in departments.items():
    # print(dept,"-->",val)
    if dept == "Finance":
        for k,v in val.items():
            val["budget"]=45

print("After modifying the budget for finance ==> ",departments)

for dept, val in departments.items():
    # print(dept,"-->",val)
    if dept == "IT":
        print("It manager: ",val["manager"])

for dept,val in departments.items():
    print(f"Department: {dept} | Manager: {val["manager"]} | Budget: {val["budget"]}")

sum=0
for dept,val in departments.items():
    sum+=val["budget"]
print("sum of all budgets:", sum)


# Sample Output

# {'HR': {'manager': 'Neha', 'budget': 25}, 'IT': {'manager': 'Arjun', 'budget': 50}, 'Finance': {'manager': 'Fatima', 'budget': 40}, 'Operations': {'manager': 'Vikram', 'budget': 35}}

# After modifying the budget for finance ==>  {'HR': {'manager': 'Neha', 'budget': 25}, 'IT': {'manager': 'Arjun', 'budget': 50}, 'Finance': {'manager': 'Fatima', 'budget': 45}, 'Operations': {'manager': 'Vikram', 'budget': 35}}

# It manager:  Arjun

# Department: HR | Manager: Neha | Budget: 25
# Department: IT | Manager: Arjun | Budget: 50
# Department: Finance | Manager: Fatima | Budget: 45
# Department: Operations | Manager: Vikram | Budget: 35

# sum of all budgets: 155
