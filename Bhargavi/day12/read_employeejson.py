#Reading the data from json then creating the new object and adding it into it
import json

#read data from json
with open("employees_data.json", "r") as f:
    python_obj = json.load(f)

employees = python_obj["employees"]

#create new object
new_employee = {
    "id": 107,
    "name": "Swathi",
    "Age": 20
}

#add that to old one
employees.append(new_employee)
print("\nUpdated Employee List:")

for emp in employees:
    print(f"ID: {emp['id']}, Name: {emp['name']}, Age: {emp['Age']}")

 
#again into json   
json_back = json.dumps(python_obj)
print("\nJSON After Adding New Employee:")
print(json_back)

with open("update_employees_data.json" ,"w") as new_file:
    json.dump(employees,new_file,indent = 2)
    

#output
# JSON After Adding New Employee:
# {
#   "employees": [
#     {
#       "id": 101,
#       "name": "Bhargavi",
#       "Age": 16
#     },
#     {
#       "id": 103,
#       "name": "Bhar",
#       "Age": 13
#     },
#     {
#       "id": 105,
#       "name": "Harsha",
#       "Age": 21
#     },
#     {
#       "id": 107,
#       "name": "Swathi",
#       "Age": 20
#     },
#     {
#       "id": 107,
#       "name": "Swathi",
#       "Age": 20
#     }
#   ]
# }