import json
employee ='''{"employees":[{"id":101,"name":"Taniya","age":22},
{"id":102,"name":"Amit","age":23}]
    }'''
# employees=json.loads(data)
# print(employees)
# print("data type: ",type(employees))
# json_data=json.dumps(employees)
# print(json_data)
# print("Data type",type(json_data))
data = json.loads(employee)
employees =data["employees"]
# print(employees)
for emp in employees:
    print(f"ID = {emp['id']},Name = {emp['name']},Age={emp['age']}")
print("Emp data to json format")
json_obj=json.dumps(employees,indent=5``)
print(json_obj)