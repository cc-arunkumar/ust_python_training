import json

data={"name":"Niranjan","age":60,"skills":["python","java"]}

json_str=json.dumps(data)
print(json_str)
print("json type",type(json_str))

python_obj=json.loads(json_str)
print(python_obj)
print("Python type:",type(python_obj))