import json

data = '''
    {
        "employees":[

            {"id":101,"name":"madhan";"age":22}          
            {"id":101,"name":"madhan";"age":22}            
        ]
    
    }
'''

employees = json.loads(data)
print(employees)
print("Type of employees",type(employees))

json_data = json.dumps(employees)
print(json_data)
print("Type of employees",type(json_data))