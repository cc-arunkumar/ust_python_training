# Writing data into the file
import csv
# sample data

data=[
    ["id","name","department","salary"],
    [101,"Vinnu","IT","20000"],
    [102,"hima","IT","300000"],
    [103,"siri","banking","200000"]
]
# Writing the data into the file

with open('employee_data2.csv',mode='w',newline='')as file:
    csv_writer=csv.writer(file)
    csv_writer.writerows(data)
print("csv writing completed")

# #sample output
# id,name,department,salary
# 101,Vinnu,IT,20000
# 102,hima,IT,300000
# 103,siri,banking,200000
