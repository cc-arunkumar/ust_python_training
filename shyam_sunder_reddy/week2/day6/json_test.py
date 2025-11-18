import json

data={"name":"shyam","age":21,"skills":["python","java"]}

json_str=json.dumps(data)
print(json_str)
# print(json_str["name"])
print(type(json_str))

python_obj=json.loads(json_str)
print(python_obj)
print(python_obj["name"])
print(type(python_obj))