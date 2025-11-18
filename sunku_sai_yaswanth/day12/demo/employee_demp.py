import json
my_employee={"id":103,"name":"yaswanth","age":22}
with open("C:/Users/Administrator/Desktop/sunku_sai_yaswanth/day12/demo/employee_data.json",mode='r')as employee_data_file:
    # read=employee_data_file.readlines()
    loading=json.load(employee_data_file)

data=loading["employee"]
# for emp in data:
#     print(emp)
data.append(my_employee)
    
# file=json.dumps(loading,indent=2)
# print(file)
with open("updated_employee_data.json",'w')as updated_data_file:
    updated_data_file.write(json.dumps(loading,indent=2))

    
