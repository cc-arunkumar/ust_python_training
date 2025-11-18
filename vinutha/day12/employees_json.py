import json
data='''
{
    "employees":[
        {"id":101,"name":"Vinnu","age":21},    
        {"id":102,"name":"hima","age":22}
        ]
}
'''
employees=json.loads(data)
print(employees)
print(type(employees))
json_data=json.dumps(employees)
print(json_data)
print(type(json_data))
