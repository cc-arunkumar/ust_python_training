# Task 3: Department Budget Tracker
# (Nested Dictionary)
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

departments["Finance"]["budget"]=45

print(departments.get("IT").get("manager"))
print(f"{departments} ",end="")
print("\n")

sum=0

for key ,value in departments.items():
    for k,v in value.items():
        if k =="budget":
            sum+=v

print(f"Total company budget:{sum}")


# EXPECTED OUTPUT
# Arjun
# {'HR': {'manager': 'Neha', 'budget': 25}, 'IT': {'manager': 'Arjun', 'budget': 50}, 'Finance': {'manager': 'Fatima', 'budget': 45}, 'Operations': {'manager': 'Vikram', 'budget': 35}} 
# Total company budget:155

