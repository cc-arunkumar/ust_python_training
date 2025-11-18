import json
json_data='''
{
    "employees":[
        {"id":101,"name":"Arun","age":16},
        {"id":102,"name":"Sai","age":32}
    ]
}
'''
data=json.loads(json_data)
employees=data["employees"]
print(employees)

for emp in employees:
    print(f"ID: {emp["id"]}, Name: {emp["name"]}, Age: {emp['age']}")

json_obj=json.dumps(employees,indent=4)
print(json_obj)