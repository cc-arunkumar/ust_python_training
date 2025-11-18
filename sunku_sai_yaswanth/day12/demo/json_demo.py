# import json
# data={"name:":"sai","age":22,"skills":['python','java']}
# json_str=json.dump(data)
# print(json_str)
# print(type(json_str))
# python_obj=json.load(json_str)
# print(python_obj)
# print(type(python_obj))

# {"name:": "sai", "age": 22, "skills": ["python", "java"]}
# <class 'str'>
# {'name:': 'sai', 'age': 22, 'skills': ['python', 'java']}
# <class 'dict'>



import json
data='''
{
   "employee": [
       {"id":101,"name":"sai","age":22},
       {"id":102,"name":"praveen","age":23}
    ]
}
'''
# employees=json.loads(data)
# print(employees)
# print(type(employees))
# json_data=json.dumps(employees)
# print(json_data)
# print(type(json_data))

# {'employee': [{'id': 101, 'name': 'sai', 'age': 22}, {'id': 102, 'name': 'praveen', 'age': 23}]}
# <class 'dict'>
# {"employee": [{"id": 101, "name": "sai", "age": 22}, {"id": 102, "name": "praveen", "age": 23}]}
# <class 'str'>


data=json.loads(data)
employee=data["employee"]
print(employee)
print("-------------------data in python format")
for emp in employee:
    print(f"Id={emp['id']},Name={emp['name']},age={emp['age']}")
print("-------------------data - json format")
json_obj=json.dumps(employee,indent=2)
print(json_obj)
