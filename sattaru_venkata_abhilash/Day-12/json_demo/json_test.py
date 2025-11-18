import json

# data={"name":'Abhi', "age":21, "skills": ['python', 'sql']}
# json_str=json.dumps(data)
# print(json_str)
# print("json_str: ", type(json_str))
# python_obj = json.loads(json_str)
# print(python_obj)
# print("python_obj: ", type(python_obj))


json_data = '''
    {
      "employees": [
        {"id":101, "name": "Abhi", "Salary":2345},
        {"id":110201, "name": "sai", "Salary":64733}
      ]
    }

'''
# employees=json.loads(data)
# print(employees)
# print(type(employees))

# json_data=json.dumps(employees,indent=2)
# print(json_data)
# print(type(json_data))


# data=json.loads(json_data)
# print(data)

# employees=data["employees"]
# print(employees)

# print("==============> Emp Data-Python Format")
# for emp in employees:
#   print(f"ID={emp['id']} ,Name={emp['name']}, Salary={emp['Salary']}")

#   print("\n\n\n")

# print("==============> Emp Data-Json Format")

# json_obj=json.dumps(employees, indent=2)
# print(json_obj)


with open ("Employee_data.json",'r') as employees_data_files:
    json_reader=json.load(employees_data_files)
    new_data={"id":102, "name": "Abhi", "Age":21}
    emp_data=json_reader['employees']
    emp_data.append(new_data)
    json_reader['employee']=emp_data

new_json=json_reader
with open("updated_data", 'w') as updated_employee_file:
    write=json.dump(updated_employee_file, indent=2) 




