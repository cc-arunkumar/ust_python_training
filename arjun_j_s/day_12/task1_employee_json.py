import json

with open("C:/Users/303391/Desktop/ust_python_training/arjun_j_s/day_12/employee_data.json","r") as employee_data_file:

    emp_data = json.load(employee_data_file)

    my_employee = {"id" : 103, "name" : "Arun" , "age" : 16}
        
    emp_data["employees"].append(my_employee)
    print(emp_data)

with open("C:/Users/303391/Desktop/ust_python_training/arjun_j_s/day_12/updated_employee_data.json","w") as updated_file:
    json.dump(emp_data,updated_file,indent=2)
