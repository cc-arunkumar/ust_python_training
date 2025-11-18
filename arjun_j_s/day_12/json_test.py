import json

# data ={"name":"Arjun","age":23,"skills":["Python","Java"]}

# json_str = json.dumps(data)
# print(json_str,type(json_str))

# py_obj = json.loads(json_str)
# print(py_obj,type(py_obj))

data = """
    {
        "employees" : [
            {"id":101,"name":"Arjun","age":23},
            {"id":102,"name":"AJS","age":23}
        ]
    }
"""

employees = json.loads(data)
print(employees,type(employees))

for emp in employees["employees"]:
    print(f"ID : {emp["id"]} Name : {emp["name"]} Age : {emp["age"]}")

json_data = json.dumps(employees,indent=2)
print(json_data,type(json_data))


