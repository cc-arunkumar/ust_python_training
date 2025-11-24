import json
data=""" 
    {
         "employees":[
            {"id":101,"name":"varsha","age":10},
            {"id":102,"name":"yashu","age":20}      
        ] 
    }
"""

employees=json.loads(data)
print(employees)
print(type(employees))

json_str=json.dumps(employees)
print(json_str)
print(type(json_str))


# Output
# {'employees': [{'id': 101, 'name': 'varsha', 'age': 10}, {'id': 102, 'name': 'yashu', 'age': 20}]}
# <class 'dict'>
# {"employees": [{"id": 101, "name": "varsha", "age": 10}, {"id": 102, "name": "yashu", "age": 20}]}
# <class 'str'>