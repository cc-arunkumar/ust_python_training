import json

with open("employees_data.json", "r") as emp_data:
    python_obj = json.load(emp_data)

employees = python_obj["employees"]
my_employee = {
    "id": 103,
    "name": "Vinutha",
    "age": 21
}
employees.append(my_employee)
print(employees)

with open("update_employee_data.json","w") as new_file:
    json.dump(employees,new_file,indent=2)

