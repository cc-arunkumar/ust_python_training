import json   

# JSON string with employee data
employees = """ 
    {
         "employees":[
            {"id":101,"name":"Shiv","age":16},
            {"id":102,"name":"Yashu","age":20}      
        ] 
    }
"""

# convert JSON string to Python dictionary
data = json.loads(employees)

# extract the list of employees
employees = data["employees"]

print("========= employee data to python object =======")

# loop through employees and print details
for emp in employees:
    print(f"ID:{emp['id']},Name:{emp['name']},age:{emp['age']}")

print("======== emp data - JSON format ========")

# convert Python object (list of employees) back to JSON string
json_obj = json.dumps(employees)

# print JSON string
print(json_obj)


#o/p:
# ========= employee data to python object =======
# ID:101,Name:Shiv,age:16
# ID:102,Name:Yashu,age:20
# ======== emp data - JSON format ========
# [{"id": 101, "name": "Shiv", "age": 16}, {"id": 102, "name": "Yashu", "age": 20}]