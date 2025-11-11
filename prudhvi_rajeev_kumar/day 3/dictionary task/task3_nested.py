departments = {
 "HR": {"manager": "Neha", "budget": 25},
 "IT": {"manager": "Arjun", "budget": 50},
 "Finance": {"manager": "Fatima", "budget": 40}
}

departments["Operations"] = {"manager": "Vikram", "budget": 35}
print(departments)

departments["Finance"]["budget"] = 45
print(departments)

print(departments["IT"]["manager"])

for dept, (manager, budget) in departments.items():
    print(f"Department : {dept} | Namager Name : {departments.get(dept)["manager"]} | Budget : {departments.get(dept)["budget"]}")

count = 0
for dept, (manager, budget) in departments.items():
    count += departments.get(dept)["budget"]
print(count)

