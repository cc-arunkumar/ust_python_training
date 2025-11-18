import json
with open("employee_data.json","r") as employee_data_file:
    data = json.load(employee_data_file)
    print(data)
    
    
my_emp ={"id" : 103 ,"name": "Mona" ,"age" : 23}

employees = data["employees"]
employees.append(my_emp)

with open("updated_employee.json" ,"w") as updated_file:
    writer=json.dump(employees,updated_file,indent=4)
    

