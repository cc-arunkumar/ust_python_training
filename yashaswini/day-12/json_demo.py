import json   # import json module

# JSON string with employee data
data = """ 
    {
         "employees":[
            {"id":101,"name":"ABC","age":30},
            {"id":102,"name":"DEF","age":10}      
        ] 
    }
"""

# convert JSON string to Python dictionary
employees = json.loads(data)
print(employees)         
print(type(employees))    

# convert Python dictionary back to JSON string
json_str = json.dumps(employees)
print(json_str)           
print(type(json_str))     


#o/p:
# {'employees': [{'id': 101, 'name': 'ABC', 'age': 30}, {'id': 102, 'name': 'DEF', 'age': 10}]}
# <class 'dict'>
# {"employees": [{"id": 101, "name": "ABC", "age": 30}, {"id": 102, "name": "DEF", "age": 10}]}
# <class 'str'>