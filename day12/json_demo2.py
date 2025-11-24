import json

with open('employees_data.json','r') as json_file:
    employees_data= json.load(json_file)

new_employee={"id":103,"name":"varsha","age":21}
employees_data["employees"].append(new_employee)
        
with open('employees_data.json','w') as json_file:
    json.dump(employees_data,json_file,indent=2)
    
with open('updated_employee_data.json','w') as updated_employee_data_file:
        json.dump(employees_data, updated_employee_data_file, indent=2)
          



# output in updated_employee_data.json
# {
#   "employees": [
#     {
#       "id": 101,
#       "name": "varsha",
#       "age": 10
#     },
#     {
#       "id": 102,
#       "name": "yashu",
#       "age": 20
#     },
#     {
#       "id": 103,
#       "name": "varsha",
#       "age": 21
#     }
#   ]
# }