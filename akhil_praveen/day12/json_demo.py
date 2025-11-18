import json

data  = {"name":"Arun","age":16,"skills":['Python','Java']}

json_str = json.dumps(data )
print(json_str)
print("json_str: ",type(json_str))

python_obj = json.loads(json_str)
print(python_obj)
print("pyhton_obj: ",type(python_obj))