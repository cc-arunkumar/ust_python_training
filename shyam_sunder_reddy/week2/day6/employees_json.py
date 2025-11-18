import json
data='''{
        "employees":[
            {"id":101,"name":"Shyam","age":21},
            {"id":102,"name":"ram","age":21}
        ]
}
'''
pydata=json.loads(data)
print(pydata,type(pydata))

jsdata=json.dumps(pydata)
print(jsdata)