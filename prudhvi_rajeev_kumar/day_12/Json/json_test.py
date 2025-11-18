import json

data = {"name" : "Rajeev", "Age" : 19, "Skills" : ['Python', 'Java']}

result = json.dumps(data)
print(result)
print(type(result))

python_obj = json.loads(result)
print(python_obj)
print(type(python_obj))

#Sample Output:
# {"name": "Rajeev", "Age": 19, "Skills": ["Python", "Java"]}
# <class 'str'>
# {'name': 'Rajeev', 'Age': 19, 'Skills': ['Python', 'Java']}
# <class 'dict'>