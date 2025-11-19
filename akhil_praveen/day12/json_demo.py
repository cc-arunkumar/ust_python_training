import json

# data  = {"name":"Arun","age":16,"skills":['Python','Java']}

# json_str = json.dumps(data )
# print(json_str)
# print("json_str: ",type(json_str))

# python_obj = json.loads(json_str)
# print(python_obj)
# print("pyhton_obj: ",type(python_obj))

data = '''
        {
        "employees":[
            {"id":101,"name":"Arun","age":16},
            {"id":102,"name":"Sai","age":32}
        ]
        }
'''

data = json.loads(data)
employees = data["employees"]
print(employees)

print("=================>Emp data - Python format")

print("\n")

for emp in employees:
    print(f"ID = {emp["id"]}, Name = {emp["name"]}, Age = {emp["age"]}")

print("\n")

print("==================> Emp data - Json format")
json_obj = json.dumps(employees,indent=2)
print(json_obj)
print(type(json_obj))