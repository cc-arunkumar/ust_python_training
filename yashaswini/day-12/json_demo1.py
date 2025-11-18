import json  

# read data from employees_data.json
with open('employees_data.json','r') as json_file:
    employees_data = json.load(json_file)

# new employee record
new_employee = {"id": 103, "name": "Lakshmi", "age": 30}

# add new employee to list
employees_data["employees"].append(new_employee)

# write updated data back to employees_data.json
with open('employees_data.json','w') as json_file:
    json.dump(employees_data, json_file, indent=2)

# also save updated data into another file
with open('updated_employee_data.json','w') as updated_employee_data_file:
    json.dump(employees_data, updated_employee_data_file, indent=2)
