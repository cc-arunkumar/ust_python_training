import json

data = {"name":"Felix","age":23,"skills":["Python"]}

json_str = json.dumps(data)
print(json_str)
print("json_str: ",type(json_str))

python_obj = json.loads(json_str)
print(python_obj)
print("python_obj: ",type(python_obj))


new_data = '''
            {
               "employees": [
                   {"id":101,"name":"Felix","age":23},
                   {"id":102,"name":"Sai","age":24}
               ]
            }
            '''
print("========= Emp Data - Python Format")
employees = json.loads(new_data)
employee = employees["employees"]
print(employee)
for emp in employee:
    print(f"ID : {emp["id"]}, Name : {emp["name"]}, Age : {emp["age"]}")
print("\n\n\n")
print("========= Emp Data - JSON Format")
json_data = json.dumps(employee,indent=2)
print(json_data)
print("json_str: ",type(json_data))