# Program which demonstrates the writing in dictionary format in csv file


import csv

employees=[
    {"id":401,"name":"varsha","department":"Development","salary":800000},
    {"id":402,"name":"yashu","department":"Development","salary":900000},
    {"id":404,"name":"bhargavi","department":"Testing","salary":1800000},
    {"id":406,"name":"vinutha","department":"support","salary":100000}   
]
with open('employee_dict_data.csv',mode='w',newline='') as file:
    header=["id","name","department","salary"]
    writer= csv.DictWriter(file,fieldnames=header)
    writer.writeheader()
    writer.writerows(employees)
print("csv writing completed")


# output
# csv writing completed
# contents in employee_dict_data.csv file
# id,name,department,salary
# 401,varsha,Development,800000
# 402,yashu,Development,900000
# 404,bhargavi,Testing,1800000
# 406,vinutha,support,100000
