#Task 1: Employee Directory System

# Dictionary representing employees with Employee ID as the key and Name as the value
employees = {
    "E101": "Arjun",
    "E102": "Neha",
    "E103": "Ravi"
}

# Adding new employees to the dictionary
employees["E104"] = "Priya"
employees["E105"] = "Vikram"

# Updating the name of the employee with ID "E103"
employees["E103"] = "Ravi Kumar"

# Deleting the employee with ID "E102"
del employees["E102"]

# Printing the total number of employees after updates
print("Total Employees: ", len(employees))

# Iterating through the dictionary to print employee ID and Name
for emp_id, name in employees.items():
    print(f"Employee ID: {emp_id} → Name: {name}")

# Attempting to get the name of an employee with ID "E110" (which does not exist)
# The second argument ("Employee not found") is returned if the key doesn't exist
name = employees.get("E110", "Employee not found")
print(name)



# Sample Execution
# Total Employees:  4
# Employee ID:E101→ Name:Arjun
# Employee ID:E103→ Name:Ravi Kumar
# Employee ID:E104→ Name:Priya
# Employee ID:E105→ Name:Vikram
# Employee not found