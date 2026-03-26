import json

data='''
    {

    "employees":[
    {"id":101,"name":"Gowtham","age":22},
    {"id":102,"name":"Dinesh","age":24}
    ]
    }

'''

# print(type(data))

data=json.loads(data)
# print(type(data))

employees=data["employees"]
print(type(employees))

print("-----> EMP to python format")

for emp in employees:
    print(f"ID :{emp["id"]},Name :{emp["name"]},Age :{emp["age"]}")

print("\n\n")

print("------------> python to json")

json_obj=json.dumps(employees,indent=2)
print(json_obj)