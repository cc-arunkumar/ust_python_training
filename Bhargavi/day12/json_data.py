import json

data = { "Name":"Bhargavi","age":16,"skills":['python','Java']}

# Convert Python object → JSON string
json_str = json.dumps(data)
print(json_str)
print("json_str:", type(json_str))

# Convert JSON string → Python object
python_obj = json.loads(json_str)
print(python_obj)
print("python_obj:", type(python_obj))

#output
# {"Name": "Bhargavi", "age": 16, "skills": ["python", "Java"]}
# json_str: <class 'str'>
# {'Name': 'Bhargavi', 'age': 16, 'skills': ['python', 'Java']}
# python_obj: <class 'dict'>