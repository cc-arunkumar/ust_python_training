import json

# data={"name":"Akshh","age":16,"skills":['python','Java']}
# json_str=json.dumps(data)
# print(json_str)
# print("json_str:",type(json_str))

# python_obj=json.loads(json_str)
# print(python_obj)
# print("python_obj:",type(python_obj))

data = """
    {
        "employees":[
            {"id":101,"name":"Akshh","age":21},
            {"id":102,"name":"rash","age":21}
        ]
    }
"""
employees=json.loads(data)
print(employees)
print(type(employees))

json_data=json.dumps(employees)
print(json_data)
print(type(json_data))

data=json.loads(json_data)
employees=data["employees"]
print(employees)
for emp in employees:
    print(f"ID={emp['id']},name={emp['name']},age=(emp['age])")
    
print("\n\n\n")
json_obj=json.dumps(employees,indent=2)
print(json_obj)
