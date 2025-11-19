import json

with open("C:/Users/303394/Desktop/ust_python_training/akhil_praveen/day12/employees_data.json","r") as employees_json_data:
    data = json.load(employees_json_data)
    employees = data["employees"]
    my_emp = {"id":103,"name":"Akhil","age":22}
    employees.append(my_emp)
    for emp in employees:
        print(f"ID = {emp["id"]}, Name = {emp["name"]}, Age = {emp["age"]}")
    data["employees"] = employees
    json_obj = json.dumps(data,indent=2)
    print(json_obj)
    # json.dump(data)
with open("C:/Users/303394/Desktop/ust_python_training/akhil_praveen/day12/employees_data.json","w") as employees_json_data:
    json.dump(data,employees_json_data,indent=2)