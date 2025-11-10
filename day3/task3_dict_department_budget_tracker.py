#department budget tracker

departments = {
    "HR": {"manager": "Neha", "budget": 25},
    "IT": {"manager": "Arjun", "budget": 50},
    "Finance": {"manager": "Fatima", "budget": 40}
}

departments.update({"operations": {"manager": "Vikram", "budget": 35}})
print(departments)


departments.update({"Finance": {"manager": "Fatima", "budget": 45}})
print(departments)


print("IT's manager name:", departments["IT"]["manager"])


for dept, info in departments.items():
    print("department:", dept, "manager:", info["manager"], "budget:", info["budget"])

# output
# IT's manager name: Arjun
# department: HR manager: Neha budget: 25
# department: IT manager: Arjun budget: 50
# department: Finance manager: Fatima budget: 45
# department: operations manager: Vikram budget: 35