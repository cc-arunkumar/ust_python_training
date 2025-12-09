import json

data = ''' 
{
    "employees": [
        {"id": 101, "name": "Bhargavi", "Age": 16},
        {"id": 103, "name": "Bhar", "Age": 13}
    ]
}
'''

employees = json.loads(data)
print(employees)
print(type(employees))

json_data = json.dumps(employees)
print(json_data)
print(type(json_data))

# {'employees': [{'id': 101, 'name': 'Bhargavi', 'Age': 16}, {'id': 103, 'name': 'Bhar', 'Age': 13}]}
# <class 'dict'>
# {"employees": [{"id": 101, "name": "Bhargavi", "Age": 16}, {"id": 103, "name": "Bhar", "Age": 13}]}
# <class 'str'>