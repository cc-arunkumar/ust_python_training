import json
employees=""" 
    {
         "employees":[
            {"id":101,"name":"varsha","age":10},
            {"id":102,"name":"yashu","age":20}      
        ] 
    }
"""

data=json.loads(employees)
employees=data["employees"]
print("========= employee data to python object =======")

for emp in employees:
    print(f"ID:{emp['id']},Name:{emp['name']},age:{emp['age']}")

print("======== emp data - JSON format")
json_obj=json.dumps(employees)
print(json_obj)


# Output
# ========= employee data to python object =======
# ID:101,Name:varsha,age:10
# ID:102,Name:yashu,age:20
# ======== emp data - JSON format
# [{"id": 101, "name": "varsha", "age": 10}, {"id": 102, "name": "yashu", "age": 20}] 