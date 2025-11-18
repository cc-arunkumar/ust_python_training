import json
with open("employees_data.json",'r') as employees_data_file:
    json_reader=json.load(employees_data_file)
    em=json_reader["employees"]
    my_employee={"id":103,"name":"Sovan","age":22}
    em.append(my_employee)
    

with open("updated_employee.json",'w') as updated_employee:
    json_write=json.dump(json_reader,updated_employee, indent=4)
    