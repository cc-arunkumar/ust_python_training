import json
data={"name":"Harsh","age":22,"skills":["python","java"]}

json_str=json.dumps(data)
print(json_str)
print(type(json_str))


py_str=json.loads(json_str)
print(py_str)
print(type(py_str))

print("\n")

data1="""
    {
        "employees":[
            {"id":101,"name":"Harsh","age":22},
            {"id":102,"name":"Rohit","age":22}
        ]
    }
"""

employees=json.loads(data1)
print(employees)
print(type(employees))
print("\n")
data2=employees["employees"]
for emp in data2:
    print(f"ID: {emp["id"]}, Name: {emp["name"]}, Age:{emp["age"]}")
print("\n")
py_data=json.dumps(data2,indent=2)
print(py_data)
print(type(py_data))



