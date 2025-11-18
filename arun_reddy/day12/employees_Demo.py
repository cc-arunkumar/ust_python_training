import json

emp={}
with open("D:/ust_python_training/arun_reddy/day12/employees_data.json","r") as employees_data_file:
    content=json.load(employees_data_file)
    emp=content["employees"]
    my_employee={"id":803,"name":"Arjun","age":24}
    emp.append(my_employee)
    print(emp)
with open("updated.json","w") as employee_updated_file:
    writes=json.dump(emp,employee_updated_file,indent=2)
        