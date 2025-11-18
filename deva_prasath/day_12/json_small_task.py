import json

with open(r'D:\training\ust_python_training\deva_prasath\day_12\employees_data.json','r') as f1:
    emp=json.load(f1)
    
data=emp["employees"]
dicti={"id":103,"name":"Deva","age":21}

data.append(dicti)
print(data)

json_format=json.dumps(data,indent=3)
print(json_format)

with open('updated_employees_data.json','w') as file:
    file.write(json.dumps(emp,indent=2))