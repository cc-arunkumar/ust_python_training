# Task 1: Employee Directory System
# Scenario:
# UST’s HR team keeps employee details in a Python dictionary.
# Each employee has a unique ID and name.
# Instructions:
# 1. Create a dictionary named employees with:
# "E101": "Arjun"
# "E102": "Neha"
# "E103": "Ravi"
# 2. Add two new employees:
# "E104": "Priya"
# "E105": "Vikram"
# 3. Update "E103" to "Ravi Kumar" .
# 4. Remove "E102" .
# 5. Display the total number of employees.
# 6. Print the final list like:
# Employee ID: E101 → Name: Arjun
# 7. If "E110" is searched, print "Employee not found" .

#code

employees = {"E101": "Arjun", "E102": "Neha", "E103": "Ravi"}
employees.update({"E104": "Priya", "E105": "Vikram"})
employees["E103"] = "Ravi Kumar"
employees.pop("E102", None)
print("Total number of employees:", len(employees))
for emp_id, name in employees.items():
    print(f"Employee ID: {emp_id} → Name: {name}")
search_id = "E110"
if search_id in employees:
    print(f"Employee ID: {search_id} → Name: {employees[search_id]}")
else:
    print("Employee not found")

#output
# PS C:\Users\303379\day3_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day3_training/Task1_Employee_Directory_System.py
# Total number of employees: 4
# Employee ID: E101 → Name: Arjun
# Employee ID: E103 → Name: Ravi Kumar
# Employee ID: E104 → Name: Priya
# Employee ID: E105 → Name: Vikram
# Employee not found