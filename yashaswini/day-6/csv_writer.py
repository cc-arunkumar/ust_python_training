# Writing data into the file
import csv
# sample data

data=[
    ["id","name","department","salary"],
    [101,"varsha","IT","20000"],
    [102,"virat","IT","300000"],
    [103,"arjun","banking","200000"]
]
# Writing the data into the file

with open('employee_data.csv',mode='w',newline='')as file:
    csv_writer=csv.writer(file)
    csv_writer.writerows(data)
print("csv writing completed")


#o/p:
# csv writing completed