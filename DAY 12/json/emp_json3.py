import json

file="DAY 12\json\employees_data.json"
new_file=r"DAY 12\\json\\updated_employees_data.json"
with open(file,"r") as employee_data:
    employee=json.load(employee_data)

my_data={
    "id":4,
    "name":"Madhan",
    "age":22
}
employee["employees"].append(my_data)


with open(new_file,"w") as updated_emp:
    updated_emp.write(json.dumps(employee, indent=3))
