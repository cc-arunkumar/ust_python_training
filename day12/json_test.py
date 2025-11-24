import json
data={"name":"varsha","age":21,"skills":['python','java']}
json_str=json.dumps(data)
print(json_str)
print(type(json_str))

python_obj=json.loads(json_str)
print(python_obj)
print(type(python_obj))