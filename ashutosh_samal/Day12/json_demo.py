import json

# Multi-line string that contains JSON data representing a list of employees
data = '''
    {
        "employees":[
            {"id":101,"name":"Arun","age":16},
            {"id":102,"name":"Sai","age":32}
        ]
    }
'''

# Convert the JSON string to a Python dictionary (with a key "employees" and a list of employee dictionaries)
employees = json.loads(data)

# Print the dictionary representation of the JSON data
print(employees)
print(type(employees))

# Convert the Python dictionary back to a JSON string (note: the 'employees' dictionary becomes a string)
json_data = json.dumps(employees)

# Print the JSON string
print(json_data)
print(type(json_data))


#Sample Output
# {'employees': [{'id': 101, 'name': 'Arun', 'age': 16}, {'id': 102, 'name': 'Sai', 'age': 32}]}
# <class 'dict'>
# {"employees": [{"id": 101, "name": "Arun", "age": 16}, {"id": 102, "name": "Sai", "age": 32}]}
# <class 'str'>