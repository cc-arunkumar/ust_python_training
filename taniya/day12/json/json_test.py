import json
data = {"name":"Taniya","age":22,"skills":["python","java"]}
json_str=json.dumps(data)
print(json_str)
print("json_str: ",type(json_str))
python_obj=json.loads(json_str)
print(python_obj)
print("python_obj",type(python_obj))