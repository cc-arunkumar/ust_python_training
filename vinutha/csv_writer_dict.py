import csv

employees=[
    {"id":401,"name":"hima","department":"Development","salary":800000},
    {"id":402,"name":"chakitha","department":"Development","salary":900000},
    {"id":404,"name":"siri","department":"Testing","salary":1800000},
    {"id":406,"name":"vinnu","department":"support","salary":100000}   
]
with open('employee_dict_data.csv',mode='w',newline='') as file:
    header=["id","name","department","salary"]
    writer= csv.DictWriter(file,fieldnames=header)
    writer.writeheader()
    writer.writerows(employees)
print("csv writing completed")