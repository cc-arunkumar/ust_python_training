import json

# Dictionary
data={"name":"Uma","id":101,"skills":["python","java"]}

# Dictionary--->json
json_str=json.dumps(data)
print(json_str)
print("Type:",type(json_str))

# json----->python_object
python_obj=json.loads(json_str)
print(python_obj)
print("Type:",type(python_obj))