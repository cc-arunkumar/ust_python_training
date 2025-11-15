employee = {
    "E101": "Arjun",
    "E102": "Neha",
    "E103": "Ravi"
}

employee["E104"] = "Madhan"
employee["E105"] = "Nawin"
employee["E103"] = "Ravikumar"

del employee["E102"]
print("updated dictionary is-->",employee)

count = 0
for key,val in employee.items():
    count += 1
print(count)

for key,val in employee.items():
        print(f"Employee ID: {key} -> {val}")