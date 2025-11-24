import json   # Import JSON module for working with JSON data

# data  = {"name":"Arun","age":16,"skills":['Python','Java']}   # Example Python dictionary

# json_str = json.dumps(data )   # Convert Python dict to JSON string
# print(json_str)                # Print JSON string
# print("json_str: ",type(json_str))   # Print type (str)

# python_obj = json.loads(json_str)    # Convert JSON string back to Python dict
# print(python_obj)                    # Print Python dict
# print("pyhton_obj: ",type(python_obj))   # Print type (dict)

data = '''
        {
        "employees":[
            {"id":101,"name":"Arun","age":16},
            {"id":102,"name":"Sai","age":32}
        ]
        }
'''   # JSON data as a raw string

data = json.loads(data)   # Parse JSON string into Python dict
employees = data["employees"]   # Extract list of employees
print(employees)   # Print employees list in Python format

print("=================>Emp data - Python format")

print("\n")

for emp in employees:   # Loop through each employee dictionary
    print(f"ID = {emp["id"]}, Name = {emp["name"]}, Age = {emp["age"]}")   # Print employee details

print("\n")

print("==================> Emp data - Json format")
json_obj = json.dumps(employees,indent=2)   # Convert Python list back to JSON string with indentation
print(json_obj)   # Print formatted JSON string
print(type(json_obj))   # Print type of json_obj (str)

# ===========================
# Expected Output:
# ===========================
# [{'id': 101, 'name': 'Arun', 'age': 16}, {'id': 102, 'name': 'Sai', 'age': 32}]
# =================>Emp data - Python format
#
# ID = 101, Name = Arun, Age = 16
# ID = 102, Name = Sai, Age = 32
#
# ==================> Emp data - Json format
# [
#   {
#     "id": 101,
#     "name": "Arun",
#     "age": 16
#   },
#   {
#     "id": 102,
#     "name": "Sai",
#     "age": 32
#   }
# ]
# <class 'str'>
