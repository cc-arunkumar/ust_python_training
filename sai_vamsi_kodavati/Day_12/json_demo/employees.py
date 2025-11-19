import json
json_data='''
    {
        "employees":[
            {"id":101,"name":"Arun","age":16},
            {"id":102,"name":"niru","age":22}
        ]
    }
'''

# employees=json.loads(data)
# print(employees)
# print(type(employees))

# python_obj=json.dumps(employees)
# print(python_obj)
# print(type(python_obj))

# data=json.loads(json_data)
# print(data)

# employee=data["employees"]
# print(employee)

# print("======> Emp data- Python Format")
# for emp in employee:
#     print(f"ID= {emp['id']}, Name= {emp['name']}, Age= {emp['age']}")

# print("\n\n\n")
# print("======> Emp data- json Format")

# json_obj=json.dumps(employee,indent=2)
# print(json_obj)

with open("employees_data.json","r") as employees_data_file:
    json_reader=json.load(employees_data_file)
    new_data={"id":103,"name":"niranjan","age":22}
    emp_data=json_reader['employees']
    emp_data.append(new_data)
    json_reader['employees']=emp_data
    
new_json=json_reader
with open("updated_employees_data.json","w") as updated_employee_file:
    write=json.dump(new_json,updated_employee_file,indent=2)