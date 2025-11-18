import json

with open(r"C:\Users\303372\Desktop\ust_python_training\Arumukesh\day_12\employees_data.json", "r") as employees_data_json:
    data = json.load(employees_data_json)

updated_employees = [{"id": 103, "name": "mukesh", "age": 10}]
data["employees"].extend(updated_employees)

with open(r"C:\Users\303372\Desktop\ust_python_training\Arumukesh\day_12\updated_employees_data.json", "w") as employees_data_json:
    json.dump(data, employees_data_json, indent=1)

print("Employee added successfully!")
