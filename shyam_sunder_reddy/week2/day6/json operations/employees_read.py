import json

with open("employees_data.json","r") as employees_data_file:
    rea=json.load(employees_data_file)
    reader=rea["employees"]
    emp={"id":103,"name":"rambo","age":70}
    reader.append(emp)

with open("updated_employees_data.json","w") as employee_write_file:
    writer=json.dump(rea,employee_write_file,indent=2)
    print(writer)    