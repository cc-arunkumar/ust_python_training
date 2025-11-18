import json

data={"name" : "Sohan", "age" : 23, "Skills" : ["Python","Java"]}

json_str = json.dumps(data)
print(json_str)
print(type(json_str))


python_object=json.loads(json_str)
print(python_object)
print(type(python_object))

dataa="""
    {
        "employees":[
            {"id": 101 , "name" : "Sohan" , "Age" : 22},
            {"id": 102 , "name" : "Pihoo" , "Age" : 20}

        ]
    }

"""

employees =json.loads(dataa)
print(employees)
print(type(employees))

#Output
# {"name": "Sohan", "age": 23, "Skills": ["Python", "Java"]}
# <class 'str'>
# {'name': 'Sohan', 'age': 23, 'Skills': ['Python', 'Java']}
# <class 'dict'>
# {'employees': [{'id': 101, 'name': 'Sohan', 'Age': 22}, {'id': 102, 'name': 'Pihoo', 'Age': 20}]} 
# <class 'dict'>
