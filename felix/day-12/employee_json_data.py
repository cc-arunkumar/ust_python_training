import json

with open("employees_data.json","r") as employee_data:
    employee = json.load(employee_data)
    emp = employee["employees"]
    
    emp.append({"id":103,"name":"Arun","age":25})
    
with open("updated_employees.json","w") as updated_file:
    updated_data = json.dump(emp,updated_file,indent=2)