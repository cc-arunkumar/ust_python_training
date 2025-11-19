import json


# data = {"name": "Rohit", "age": 25, "city": "New York"}

# print(type(data))


# json_str = json.dumps(data)
# print("JSON String:", json_str)
# # print("JSON String:", json_str.get("name","No Name"))
# print("json type:", type(json_str))


# pytho_obj = json.loads(json_str)
# print("Python Object:", pytho_obj)  
# print("python type:", type(pytho_obj))


data1 = '''
{
        "employees":[
            {"id":101, "name":"ABC","age":16},
            {"id":102, "name":"DEF","age":32},
            {"id":103, "name":"XYZ","age":48}
        ]
}

'''

final_data = json.loads(data1)
print(final_data)
# print(type(employees))

employees = final_data["employees"]
print(employees)
print(type(employees))

for emp in employees:
    print(f"ID: {emp['id']}, Name: {emp['name']}, Age: {emp['age']}")



# json_data = json.dumps(employees)
# print(json_data)
# print(type(json_data))


# import json

# data1 = """
# {
#     "employees":[
#         {"id":101, "name":"ABC","age":16},
#         {"id":102, "name":"DEF","age":32},
#         {"id":103, "name":"XYZ","age":48}
#     ]
# }
# """

# employees = json.loads(data1)
# print(employees)
# print(type(employees))   # dict

# json_data = json.dumps(employees)
# print(json_data)
# print(type(json_data))   # str
