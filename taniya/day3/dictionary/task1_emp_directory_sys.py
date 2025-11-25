# Create a simple dictionary
dect = {"key": "values"}

# Employee dictionary with initial data
employee = {"E101": "arjun", "E102": "neha", "E103": "ravi"}

# Add new employees
employee["E104"] = "priya"
employee["E105"] = "vikram"

# Print dictionary after adding employees
print(employee)

# Update an existing employee's name
employee["E103"] = "ravi kumar"
print("after updating name:", employee)

# Delete an employee record
del employee["E102"]
print("after deleting E102:", employee)

# Print total number of employees
print("total no. of employees", len(employee))

# Loop through dictionary and print employee details
for employee_id, name in employee.items():
    print(f"employee id:{employee_id}-> Name:{name}")

# Use get() method to safely access a key that may not exist
print(employee.get("E10", "employees not found"))

# -------------------------
# Expected Output:
# {'E101': 'arjun', 'E102': 'neha', 'E103': 'ravi', 'E104': 'priya', 'E105': 'vikram'}
# after updating name: {'E101': 'arjun', 'E102': 'neha', 'E103': 'ravi kumar', 'E104': 'priya', 'E105': 'vikram'}
# after deleting E102: {'E101': 'arjun', 'E103': 'ravi kumar', 'E104': 'priya', 'E105': 'vikram'}
# total no. of employees 4
# employee id:E101-> Name:arjun
# employee id:E103-> Name:ravi kumar
# employee id:E104-> Name:priya
# employee id:E105-> Name:vikram
# employees not found