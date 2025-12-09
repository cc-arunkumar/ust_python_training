import json

# JSON string
data = ''' 
{
    "employees": [
        {"id": 101, "name": "Bhargavi", "Age": 16},
        {"id": 103, "name": "Bhar", "Age": 13}
    ]
}
'''

# Convert JSON string → Python dict
python_obj = json.loads(data)
print(python_obj)
print(type(python_obj))

# Access employees list
employees = python_obj["employees"]
print("Employees list:", employees)

# Loop and print formatted
print("\nFormatted Output:")
for emp in employees:
    print("ID: {0}, Name: {1}, Age: {2}".format(emp["id"], emp["name"], emp["Age"]))

# Convert Python dict → JSON string again
json_back = json.dumps(python_obj)
print("\nConverted Back to JSON:")
print(json_back )
print(type(json_back))
