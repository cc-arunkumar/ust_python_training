import json
with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\taniya\day12\json\employees_data_json.json","r") as file:
    data=json.load(file)
    my_emp=data["employees"]
    new_emp={"id":103,"name":"manya","age":22}
    my_emp.append(new_emp)
with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\taniya\updated_employee_data_json.json","w") as file1:
    writer=json.dump(my_emp, file1,indent=2)