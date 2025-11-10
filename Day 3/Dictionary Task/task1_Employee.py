employee = {"E101": "Arjun" , "E102": "Neha" , "E103": "Ravi" }
print(employee)
employee["E103"] = "Priya"
employee["E105"] = "Vikram"
employee["E102"] = "Ravi Kumar"
del employee["E102"]
print(len(employee))
for key, value in employee.items():
    print(f"Employee Id : {key} -> Name : {value}")

value = employee.get("E110", "Employee Not Found")
print(value)



