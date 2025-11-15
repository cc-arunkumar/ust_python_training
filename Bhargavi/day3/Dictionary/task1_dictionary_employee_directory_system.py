#Employee Directory System

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


employees = {"E101": "Arjun","E102": "Neha","E103": "Ravi"}   # initial dictionary of employees

employees["E104"] = "Priya"      # add new employee
employees["E105"] = "Vikaram"    # add another employee

employees["E103"] = "RAvi Kumar" # update existing employee name

employees.pop("E102")            # remove employee with ID E102

total_employees = len(employees) # count total employees
print(total_employees)

print("Final employee list: ")
for emp_id , name in employees.items():   # loop through dictionary
    print(f"Employee ID : {emp_id} -> Name: {name} ")

search_id = "E110"                        # search for employee ID
if search_id in employees:
    print(f"\nEmployee ID: {search_id} -> Name: {employees[search_id]}")
else:
    print("\nEmployee not found")

# Output:
# 4

# Final employee list: 
# Employee ID : E101 -> Name: Arjun 
# Employee ID : E103 -> Name: RAvi Kumar 
# Employee ID : E104 -> Name: Priya 
# Employee ID : E105 -> Name: Vikaram 

# Employee not found