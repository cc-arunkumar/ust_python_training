#Task 1: Employee Directory System

employees={"E101": "Arjun","E102": "Neha","E103": "Ravi"}

employees["E104"]="Priya"
employees["E105"]="Vikram"
employees["E103"]="Ravi Kumar"
del employees["E102"]

print("Total Employees: ",len(employees))

for emp_id,name in employees.items():
    print(f"Employee ID:{emp_id}→ Name:{name}")

name = employees.get("E110","Employee not found")
print(name)


# Sample Execution
# Total Employees:  4
# Employee ID:E101→ Name:Arjun
# Employee ID:E103→ Name:Ravi Kumar
# Employee ID:E104→ Name:Priya
# Employee ID:E105→ Name:Vikram
# Employee not found