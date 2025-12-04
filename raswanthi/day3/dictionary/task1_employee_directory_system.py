#Task 1: Employee Directory system
employees = {
    "E101": "Arjun",
    "E102": "Neha",
    "E103": "Ravi"
}

employees["E104"] = "Priya"
employees["E105"] = "Vikram"

employees["E103"] = "Ravi Kumar"

employees.pop("E102", None)
print(f"Total number of employees: {len(employees)}")

for empl_id, name in employees.items():
    print(f"Employee ID: {empl_id} → Name: {name}")


search_item = "E110"
if search_item in employees:
    print(f"Employee ID: {search_item} → Name: {employees[search_item]}")
else:
    print("Employee not found")

'''
output:
Total number of employees: 4
Employee ID: E101 → Name: Arjun
Employee ID: E103 → Name: Ravi Kumar
Employee ID: E104 → Name: Priya
Employee ID: E105 → Name: Vikram
Employee not found
'''