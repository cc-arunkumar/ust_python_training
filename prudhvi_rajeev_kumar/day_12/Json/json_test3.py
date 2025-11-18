import json
data = '''
      {
          "employees" : [
              {"id" : 123, "name" : "Rajeev", "salary" : 50000},
              {"id" : 345, "name" : "prudhvi", "salary" : 1000000} 
          ]
      }
'''

employees = json.loads(data)
new_employees = data["employees"]
print(employees)
# for emp in new_employees:
#     print(f"Id is : {emp["id"]}, Name is : {emp["name"]}, Salary is : {emp["salary"]}")

json_format = json.dumps(employees, indent=3)
print(json_format)
