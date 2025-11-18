import json
data = '''
      {
          "employees" : [
              {"id" : 123, "name" : "Rajeev", "salary" : 50000},
              {"id" : 345, "name" : "prudhvi", "salary" : 1000000} 
          ]
      }
'''
print(data)
print(json.loads(data))
print(type(json.loads(data)))
print(json.dumps(json.loads(data)))
print(type(json.dumps(json.loads(data))))

#Sample Output:

#       {
#           "employees" : [
#               {"id" : 123, "name" : "Rajeev", "salary" : 50000},   
#               {"id" : 345, "name" : "prudhvi", "salary" : 1000000}
#           ]
#       }

# {'employees': [{'id': 123, 'name': 'Rajeev', 'salary': 50000}, {'id': 345, 'name': 'prudhvi', 'salary': 1000000}]}  
# <class 'dict'>
# {"employees": [{"id": 123, "name": "Rajeev", "salary": 50000}, {"id": 345, "name": "prudhvi", "salary": 1000000}]}  
# <class 'str'>