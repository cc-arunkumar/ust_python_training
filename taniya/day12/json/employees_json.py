import json
data ='''{"employees":[{"id":101,"name":"Taniya","age":22},
{"id":102,"name":"Amit","age":23}]
    }'''
employees=json.loads(data)
print(employees)
print("data type: ",type(employees))
json_data=json.dumps(employees)
print(json_data)
print("Data type",type(json_data))