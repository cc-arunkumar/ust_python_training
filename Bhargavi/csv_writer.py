import csv
data=[
    ["id","name","department","salary"],
    [101,"Bhargavi","IT","20000"],
    [102,"Meena","IT","300000"],
    [103,"shero","banking","200000"]
]

with open('employee_data2.csv',mode='w',newline='')as file:
    csv_writer=csv.writer(file)
    csv_writer.writerows(data)
print("csv writing completed")
