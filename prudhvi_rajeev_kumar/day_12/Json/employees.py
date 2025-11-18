import json

file_path = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_12\employees_data.json"
with open(file_path, mode='r', encoding='utf-8') as employee:
    json_reader = json.load(employee)
    emp = json_reader["employees"]

    new_employee = {"id": 456, "name": "Kumar", "age": 23}
    emp.append(new_employee)
    
with open("updated_employees.json", mode='w', encoding='utf-8') as updated_employees:
    json.dump(json_reader, updated_employees, indent=2)
