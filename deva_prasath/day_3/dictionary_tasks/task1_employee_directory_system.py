# employee_directory_system
# UST’s HR team keeps employee details in a Python dictionary.
# Each employee has a unique ID and name.

# Dictionary storing employee IDs and names
employees = {"E101": "Arjun", "E102": "Neha", "E103": "Ravi"}

# Add new employees to the dictionary
employees["E104"] = "Priya"
employees["E105"] = "Vikram"
print(employees)  # Print the updated employee dictionary

# Update an employee's name
employees["E103"] = "Ravi Kumar"

# Remove an employee from the dictionary
del employees["E102"]

# Print the number of employees left in the dictionary
print(len(employees))

# Iterate through the dictionary and print employee details
for key, value in employees.items():
    print(f"Employee ID: {key}-->Name: {value}")

# Check if an employee with ID "E100" exists in the dictionary
if employees.get("E100") == None:
    print("Employee not found")  # Print message if employee is not found



#Sample output

# {'E101': 'Arjun', 'E102': 'Neha', 'E103': 'Ravi', 'E104': 'Priya', 'E105': 'Vikram'}
# 4
# Employee ID: E101-->Name:Arjun
# Employee ID: E103-->Name:Ravi Kumar
# Employee ID: E104-->Name:Priya
# Employee ID: E105-->Name:Vikram
# Employee not found