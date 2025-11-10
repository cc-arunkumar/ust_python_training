departments = {"HR": {"manager": "Neha", "budget": 25}, "IT": {"manager": "Arjun", "budget": 50},
               "Finance": {"manager": "Fatima", "budget": 40}}

departments["Operations"] = {"manager": "Vikram", "budget": 35}
print(departments)


for item in departments:
    if item=="Finance":
        departments[item]["budget"] = 100
print(departments)

for item in departments:
  print(departments[item]["manager"])

for item in departments:
    print("Department ",item,"| Manager ",departments[item]["manager"],"| Budget" ,departments[item]["budget"] )

# =============sample-output======================
# {'HR': {'manager': 'Neha', 'budget': 25}, 'IT': {'manager': 'Arjun', 'budget': 50}, 'Finance': {'manager': 'Fatima', 'budget': 40}, 'Operations': {'manager': 'Vikram', 'budget': 35}}
# {'HR': {'manager': 'Neha', 'budget': 25}, 'IT': {'manager': 'Arjun', 'budget': 50}, 'Finance': {'manager': 'Fatima', 'budget': 100}, 'Operations': {'manager': 'Vikram', 'budget': 35}}
# Neha
# Arjun
# Fatima
# Vikram
# Department  HR | Manager  Neha | Budget 25
# Department  IT | Manager  Arjun | Budget 50
# Department  Finance | Manager  Fatima | Budget 100
# Department  Operations | Manager  Vikram | Budget 35