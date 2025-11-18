import json

# Creating a Python dictionary with some personal data
data = {"name": "Arun", "age": 16, "skills": ['python', 'Java']}

# Convert the Python dictionary to a JSON string
json_str = json.dumps(data)
print(json_str)
# Print the type of json_str to confirm it's a string
print("json_str: ", type(json_str))

# Convert the JSON string back into a Python object (dictionary)
python_obj = json.loads(json_str)
print(python_obj)
# Print the type of python_obj to confirm it's a dictionary
print("python_obj: ", type(python_obj))


#Sample Output
# {"name": "Arun", "age": 16, "skills": ["python", "Javav"]}
# json_str:  <class 'str'>
# {'name': 'Arun', 'age': 16, 'skills': ['python', 'Javav']}      
# python_obj:  <class 'dict'>