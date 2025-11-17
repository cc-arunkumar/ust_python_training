import json
# string file 
data='''
     {
     "employees":[
     {"id":101,"name":"Rohan","age":20},
     {"id":102,"name":"yuvaraj","age":25}
     ]
     }
'''

# json----->python_obj
python_obj=json.loads(data)
print(python_obj)
print(type(python_obj))

# python_obj(dict)----->json
json_data=json.dumps(python_obj)
print(json_data)
print(type(json_data))