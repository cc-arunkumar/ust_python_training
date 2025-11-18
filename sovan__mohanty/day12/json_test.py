import json
data={"name":"Arjun","age":16,"skills":['Python','Java']}
json_str=json.dumps(data)
print(json_str)
print(type(json_str))
python_obj=json.loads(json_str)
print(python_obj)
print(type(python_obj))

#Sample Execution
# {"name": "Arjun", "age": 16, "skills": ["Python", "Java"]}
# <class 'str'>
# {'name': 'Arjun', 'age': 16, 'skills': ['Python', 'Java']}
# <class 'dict'>
