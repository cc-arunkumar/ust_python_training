import json

# Open the existing JSON file containing employee data
with open("employees_data.json", "r") as employee_data:
    # Load the JSON data into a Python dictionary
    employee = json.load(employee_data)
    # Extract the list of employees
    emp = employee["employees"]
    
    # Add a new employee to the list
    emp.append({"id": 103, "name": "Arun", "age": 25})
    
# Write the updated employee list to a new JSON file
with open("updated_employees.json", "w") as updated_file:
    # Dump the updated list as JSON with indentation for readability
    updated_data = json.dump(emp, updated_file, indent=2)
