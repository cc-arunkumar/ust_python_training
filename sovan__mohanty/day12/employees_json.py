import json
data='''
{
    "employees":[
        {"id":101,"name":"Arun","age":16},
        {"id":102,"name":"Sai","age":32}
    ]
}
'''
employees=json.loads(data)
print(employees)
print(type(employees))

json_data=json.dumps(employees)
print(json_data)
print(type(json_data))


#Sample Execution
# {'employees': [{'id': 101, 'name': 'Arun', 'age': 16}, {'id': 102, 'name': 'Sai', 'age': 32}]}
# <class 'dict'>
# {"employees": [{"id": 101, "name": "Arun", "age": 16}, {"id": 102, "name": "Sai", "age": 32}]}
# <class 'str'>