import json
json_data='''
{
    "employees":[
        {"id":101,"name":"virat","age":40},
        {"id":102,"name":"dhoni","age":42}
    ]
}
'''
# employees=json.loads(data)
# print(employees)
# print(type(employees))

# json_data=json.dumps(employees)
# print(json_data)
# print(type(json_data))


data=json.loads(json_data)
employees=data["employees"]
print(employees)

print("=>>>>>>>>>>>>>>Emp data -Python format")
for emp in employees:
    print(f"ID={emp['id']},Name={emp['name']},Age={emp['age']}")

print("=>>>>>>>>>>>>>>Emp data -Python format")

json_format=json.dumps(employees,indent=2)
print(json_format)

