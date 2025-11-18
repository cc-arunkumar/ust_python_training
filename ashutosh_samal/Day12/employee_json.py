import json

# Open and load the existing employee data from a JSON file
with open("ashutosh_samal\Day12\employees_data.json", "r") as employee_json_file:
    emp = json.load(employee_json_file)  
    
# Extract the "employees" list from the loaded JSON data
employees = emp["employees"]
print(employees)  

# Create a new employee dictionary to add to the list
new_employee = {"id": 103, "name": "Ashutosh", "age": 22}

# Append the new employee dictionary to the list of employees
employees.append(new_employee)

# Open a new file to write the updated list of employees back to JSON format
with open("updated_employee_data.json", "w") as updated_file:
    updated_file.write(json.dumps(employees, indent=2))
