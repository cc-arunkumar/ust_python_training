import json

my_info={"id":103,"name":"praveen","age":21}

with open("employees.json","r") as employee_data_file:
    employee_data_json_file=json.load(employee_data_file)
    # print(employee_data_json_file)

    employee_data_json_file['employee']+=[my_info]
    # print(employee_data_json_file)

    with open("updated_employee.json","w") as updated_file:
        writer=json.dump(employee_data_json_file,updated_file,indent=2)



