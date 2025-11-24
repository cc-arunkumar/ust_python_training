import json   # Import JSON module

# Open JSON file in read mode
with open("C:/Users/303394/Desktop/ust_python_training/akhil_praveen/day12/employees_data.json","r") as employees_json_data:
    data = json.load(employees_json_data)   # Load JSON data into Python dict
    employees = data["employees"]           # Extract employees list
    my_emp = {"id":103,"name":"Akhil","age":22}   # New employee record
    employees.append(my_emp)                # Append new employee to list
    
    # Print employee details
    for emp in employees:
        print(f"ID = {emp["id"]}, Name = {emp["name"]}, Age = {emp["age"]}")
    
    data["employees"] = employees           # Update dict with modified employees list
    json_obj = json.dumps(data,indent=2)    # Convert dict back to JSON string
    print(json_obj)                         # Print formatted JSON string
    # json.dump(data)                       # Example of dumping directly (commented out)

# Open JSON file in write mode and save updated data
with open("C:/Users/303394/Desktop/ust_python_training/akhil_praveen/day12/employees_data.json","w") as employees_json_data:
    json.dump(data,employees_json_data,indent=2)   # Write updated JSON back to file

# ===========================
# Expected Output (example):
# ===========================
# ID = 101, Name = Arun, Age = 16
# ID = 102, Name = Sai, Age = 32
# ID = 103, Name = Akhil, Age = 22
#
# {
#   "employees": [
#     {
#       "id": 101,
#       "name": "Arun",
#       "age": 16
#     },
#     {
#       "id": 102,
#       "name": "Sai",
#       "age": 32
#     },
#     {
#       "id": 103,
#       "name": "Akhil",
#       "age": 22
#     }
#   ]
# }
