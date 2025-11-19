import json

with open('employee_data.json',mode='r')as emp_data_file:
    reader=json.load(emp_data_file)
    
    my_emp={"id":103,"name":"sindhu","age":22}
    
    reader["employees"].append(my_emp)

with open('updated_emp.json',"w")as upd_emp:
    json.dump(reader,upd_emp,indent=3)

