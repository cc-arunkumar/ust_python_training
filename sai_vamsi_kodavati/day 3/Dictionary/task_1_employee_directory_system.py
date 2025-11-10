# TASK 1 -  Employee Directory System

employees = {"E101": "Arjun","E102": "Neha","E103": "Ravi"}

employees["E104"] = "Priya"
employees["E105"] = "Vikram"

employees["E103"] = "Ravi Kumar"

employees.pop("E102")

print("Total number of employees:",len(employees))

for emp_id, name in employees.items():
    print(f"Employee ID: {emp_id}, Name: {name}")

print()


emp_id = "E110"
if emp_id in employees:
    print(f"Employee ID: {emp_id},Name: {employees[emp_id]}")
else:
    print("Employee not found")

# ----------------------------------------------------------------------------------

# Sample Output

# Total number of employees: 4
# Employee ID: E101, Name: Arjun
# Employee ID: E103, Name: Ravi Kumar
# Employee ID: E104, Name: Priya
# Employee ID: E105, Name: Vikram

# Employee not found
