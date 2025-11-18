import json
data='''
{
    "employees":[
        {"id":801,"name":"Arun","age":16},
        {"id":802,"name":"sai","age":32}
    ]
      }
'''
      
#loads converts json into python
python_strg=json.loads(data)
print(python_strg)
print(type(python_strg))

json_strg=json.dumps(python_strg)
print(json_strg)
print(type(json_strg))