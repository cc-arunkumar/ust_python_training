import json

file_path = "Day12\\json\\json_input.json"
output_path = "Day12\\json\\json_output.json"

my_employee = {"id": 101, "name": "madhan", "age": 22}


with open(file_path, "r") as employee_details_upd:
    data = json.load(employee_details_upd)

data["employees"].append(my_employee)

with open(output_path, "w") as employee_details_upd:
    json.dump(data, employee_details_upd, indent=2)
