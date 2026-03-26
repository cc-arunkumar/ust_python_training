import json

"""data={
    "name":"Gowtham",
    "age":21,
    "skills":["C++","DSA"]
}

json_str=json.dumps(data)
print(json_str)
print(type(json_str))

obj=json.loads(json_str)
print(obj)
print(type(obj))"""


data='''
    {

    "employees":[
    {"id":101,"name":"Gowtham","age":22},
    {"id":102,"name":"Dinesh","age":24}
    ]
    }

'''

employees=json.loads(data)
print(employees)
print(type(employees))

json_data=json.dumps(employees)
print(json_data)
print(type(json_data))