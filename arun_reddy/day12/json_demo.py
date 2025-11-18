import json 

data={"name":"Arun","age":16,"skills":["Python","Java"]}

# converting into json
json_str=json.dumps(data)
print(json_str)
print("type is",type(json_str))

# converting into python
python_obj=json.loads(json_str)
print(python_obj)
print("type is ",type(python_obj))
