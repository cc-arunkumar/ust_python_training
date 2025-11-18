import json
data='''{
        "employees":[
            {"id":101,"name":"Shyam","age":21},
            {"id":102,"name":"ram","age":21}
        ]
}
'''

#changing from json format to python
pydata=json.loads(data)

employees=pydata["employees"]
for emp in employees:
    print(f"ID= {emp["id"]} | Name= {emp["name"]} | Age= {emp["age"]}")


print("===========================")

#changing from python to json
json_data=json.dumps(pydata,indent=2)
print(json_data)

