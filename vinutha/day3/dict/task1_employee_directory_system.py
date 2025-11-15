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

# Create a dictionary of employees with Employee ID as key and Name as value
employees = {"E101": "Arjun", "E102": "Neha", "E103": "Ravi"}

# Add new employees to the dictionary using update()
employees.update({"E104": "Priya", "E105": "Vikram"})

# Update the name of an existing employee (E103 → Ravi Kumar)
employees["E103"] = "Ravi Kumar"

# Remove an employee (E102) safely using pop()
# The second argument 'None' ensures no error if the key doesn't exist
employees.pop("E102", None)

# Print the total number of employees in the dictionary
print("Total number of employees:", len(employees))

# Loop through the dictionary and print each employee's ID and name
for emp_id, name in employees.items():
    print(f"Employee ID: {emp_id} → Name: {name}")

# Search for a specific employee ID
search_id = "E110"
if search_id in employees:
    # If found, print the employee details
    print(f"Employee ID: {search_id} → Name: {employees[search_id]}")
else:
    # If not found, display a message
    print("Employee not found")

#output
# PS C:\Users\303379\day3_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day3_training/Task1_Employee_Directory_System.py
# Total number of employees: 4
# Employee ID: E101 → Name: Arjun
# Employee ID: E103 → Name: Ravi Kumar
# Employee ID: E104 → Name: Priya
# Employee ID: E105 → Name: Vikram
# Employee not found