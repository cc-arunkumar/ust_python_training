import json

with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day12\json\employees_data.json") as json_data_file:
    j1=json.load(json_data_file)
    emp=j1["employees"]
    new_emp={"id":103,"name":"Neha","age":23}
    emp.append(new_emp)

with open("updated_employees_data_json.json","w") as json_data_file1:
    writer=json.dump(j1,json_data_file1,indent=2)
    