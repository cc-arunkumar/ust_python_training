import json

json_data = '''
{
  "employees": [
    {"id": 101, "name": "madhan", "age": 22},
    {"id": 102, "name": "madhan", "age": 22}
  ]
}
'''

# Parse JSON string -> Python dict
data = json.loads(json_data)
print(data)

employees = data["employees"]
print(employees)

print("==============>")

for emp in employees:
    print(f"id : {emp['id']} name : {emp['name']} age : {emp['age']}")

print("\n\n\n")
print("==============>")

# Convert Python object back to JSON string (pretty-printed)
json_obj = json.dumps(employees, indent=2)
print(json_obj)