# Task 1: Employee Directory System

employees = {
    "E101": "Arjun",
    "E102": "Neha",
    "E103": "Ravi"
}


employees["E104"] = "Priya"
employees["E105"] = "Vikram"

employees["E103"] = "Ravi Kumar"

employees.pop("E102")

print("Total Employees:", len(employees))

print("\nFinal Employee Directory:")
for emp_id, name in employees.items():
    print(f"Employee ID: {emp_id} → Name: {name}")

search_id = "E110"
if search_id in employees:
    print(f"\nEmployee ID: {search_id} → Name: {employees[search_id]}")
else:
    print("\nEmployee not found")


#sample output
# Total Employees: 4

# Final Employee Directory:
# Employee ID: E101 → Name: Arjun
# Employee ID: E103 → Name: Ravi Kumar
# Employee ID: E104 → Name: Priya
# Employee ID: E105 → Name: Vikram

# Employee not found
