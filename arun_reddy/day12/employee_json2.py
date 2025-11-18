import json
json_data='''
{
    "employees":[
        {"id":801,"name":"Arun","age":16},
        {"id":802,"name":"sai","age":32}
    ]
      }
'''
print(json_data)
#converting into python
data=json.loads(json_data)

employees=data["employees"]
print("==================Employee data in python==============")
print(employees)
print(type(employees))
for row in employees:
    print(f"id :{row["id"]} Name:{row["name"]} Age:{row["age"]}")
    

print("\n")
print("==================Employee data into json==============")

#converting into json 
# by giving teh indent=2 it make sthe json structure pretiier
json_obj=json.dumps(employees,indent=2)
print(json_obj)

    