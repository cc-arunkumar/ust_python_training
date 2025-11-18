import json

# Multi-line string representing the JSON data with employee details
json_data = '''
    {
        "employees":[
            {"id":101,"name":"Arun","age":16},
            {"id":102,"name":"Sai","age":32}
        ]
    }
'''

# Convert the JSON string into a Python dictionary
data = json.loads(json_data)

# Extract the list of employees from the loaded JSON data
employees = data["employees"]


print("==============> Emp Data - Python Format <==================")
# Loop through the list of employees and print each employee's details
for emp in employees:
    print(f"ID:{emp['id']}, Name:{emp['name']}, Age:{emp['age']}")

print("\n\n\n")


print("==============> Emp Data - JSON Format <==================")
# Convert the employee list back to JSON format with indentation
json_obj = json.dumps(employees, indent=2)
# Print the JSON-formatted employee data
print(json_obj)




#Sample Employee
# ==============> Emp Data - Python Format <==================
# ID:101, Name:Arun, Age:16
# ID:102, Name:Sai, Age:32




# ==============> Emp Data - JSON Format <==================
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