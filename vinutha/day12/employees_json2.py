import json

json_data = '''
{  
    "employees":[
        {"id":101,"name":"Vinnu","age":21},    
        {"id":102,"name":"hima","age":22}
    ]
}'''

data = json.loads(json_data)
employees = data["employees"]

print(employees)
print("========> Emp data - python format")

for emp in employees:
    print(f"ID={emp['id']}, Name={emp['name']}, Age={emp['age']}")

print("\n\n\n")
print("== emp data")
json_obj = json.dumps(employees, indent=2)
print(json_obj)
