import json 

# Create a Python dictionary
data = {"name": "Yashaswini", "age": 1, "skills": ['python', 'java']}

# Convert Python dictionary to JSON string
json_str = json.dumps(data)
print(json_str)          # Print the JSON string
print(type(json_str))    # Show its type (str)

# Convert JSON string back to Python dictionary
python_obj = json.loads(json_str)
print(python_obj)        # Print the Python object (dict)
print(type(python_obj))  # Show its type (dict)


# o/p:
# {"name": "Yashaswini", "age": 1, "skills": ["python", "java"]}
# <class 'str'>
# {'name': 'Yashaswini', 'age': 1, 'skills': ['python', 'java']}
# <class 'dict'>