# Task 1: Employee Directory System
# Scenario:
# UST’s HR team keeps employee details in a Python dictionary.
# Each employee has a unique ID and name.


# task1-employee_directory_System

employee = {
"E101": "Arjun",
"E102": "Neha",
"E103": "Ravi"
}

# add new employees
employee["E104"] = "madhan"
employee["E105"] = "nawin"

# update employee details
employee["E103"] = "Ravikumar"
# print(employee)

#remove employee details
del employee["E102"]
print(employee)

#tot num of employees

print(len(employee))

for key,value in employee.items():
    print(f"Employee ID:E101->{value}:{key}")

print(employee.get("E110","Employee not found"))

# sample output:
# {'E101': 'Arjun', 'E103': 'Ravikumar', 'E104': 'madhan', 'E105': 'nawin'}
# 4
# Employee ID:E101->Arjun:E101
# Employee ID:E101->Ravikumar:E103
# Employee ID:E101->madhan:E104
# Employee ID:E101->nawin:E105
# Employee not found