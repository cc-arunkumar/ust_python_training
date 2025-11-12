#writing into a csv file

import csv
data=[
    ["id","name","department","salary"],
    [101,"varsha","IT","20000"],
    [102,"vinutha","IT","300000"],
    [103,"yashu","banking","200000"]
]

with open('employee_data2.csv',mode='w',newline='')as file:
    csv_writer=csv.writer(file)
    csv_writer.writerows(data)
print("csv writing completed")



# output:
# id,name,department,salary
# 101,varsha,IT,20000
# 102,vinutha,IT,300000
# 103,yashu,banking,200000
