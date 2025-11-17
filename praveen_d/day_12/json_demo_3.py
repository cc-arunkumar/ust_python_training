import json

json_data='''
    {
    "employee":[
     {"id":101,"name":"Rohan","age":20},
     {"id":102,"name":"yuvaraj","age":25}
    ]
    }
'''


data=json.loads(json_data)

employess=data["employee"]
print(employess)
print(type(employess))

print("emp-data python formate")

for emp in employess:
    print(f"{emp['id']} {emp['name']},{emp['age']}")



    # emp-data json formate

    json_obj=json.dumps(employess,indent=2)
    print(json_obj)
