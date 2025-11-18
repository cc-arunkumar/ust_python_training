import json 
# data ={'name':'anjan','age': 21,'skills':['python','java']}

# json_str = json.dumps(data)
# print(json_str,type(json_str))

# json_obj = json.loads(json_str)
# print(json_obj,type(json_obj))

data = '''
{
    "employees" : [
        { "id":101,"name":"Arun","age":29 },
        { "id":102,"name":"Anjan","age":22 }
    ]
}
'''

# employees = json.loads(data)
# print(employees,type(employees))

# json_str = json.dumps(employees)
# print(json_str,type(json_str))

# employees = json.loads(data)
# print(employees,type(employees))

# employees_data = employees['employees']
# print(employees_data)

# for emp in employees_data:
#     print(f"ID:{emp['id']}\n Name: {emp['name']} \n Age: {emp['age']}")


# json_str = json.dumps(employees_data,indent=2)
# print(json_str,type(json_str))

with open('employees_data.json','r') as f:
    reader = json.load(f)
    new_employee={'id':103,'name':'Shyam','age':23}
    emp_data = reader['employees']
    emp_data.append(new_employee)
    reader['employees'] = emp_data 
    
updated_json = reader

with open('employees_data_updated.json','w') as f:
    writer = json.dump(updated_json,f,indent=3)