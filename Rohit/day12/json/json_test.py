import json   # Import JSON module

# Example dictionary (commented out)
# data = {"name": "Rohit", "age": 25, "city": "New York"}
# json_str = json.dumps(data)   # Convert Python dict → JSON string
# pytho_obj = json.loads(json_str)   # Convert JSON string → Python dict

# JSON string with employees data
data1 = '''
{
        "employees":[
            {"id":101, "name":"ABC","age":16},
            {"id":102, "name":"DEF","age":32},
            {"id":103, "name":"XYZ","age":48}
        ]
}
'''

# Deserialize JSON string → Python dict
final_data = json.loads(data1)
print(final_data)   # Prints the whole dictionary

# Extract "employees" list
employees = final_data["employees"]
print(employees)          # Prints list of employee dicts
print(type(employees))    # Shows it's a Python list

# Iterate through employees and print details
for emp in employees:
    print(f"ID: {emp['id']}, Name: {emp['name']}, Age: {emp['age']}")

# Example of converting Python object back to JSON string (commented out)
# json_data = json.dumps(employees)
# print(json_data)
# print(type(json_data))   # str


# ============sample output================
# {'employees': [{'id': 101, 'name': 'ABC', 'age': 16}, {'id': 102, 'name': 'DEF', 'age': 32}, {'id': 103, 'name': 'XYZ', 'age': 48}]}
# [{'id': 101, 'name': 'ABC', 'age': 16}, {'id': 102, 'name': 'DEF', 'age': 32}, {'id': 103, 'name': 'XYZ', 'age': 48}]
# <class 'list'>
# ID: 101, Name: ABC, Age: 16
# ID: 102, Name: DEF, Age: 32
# ID: 103, Name: XYZ, Age: 48
