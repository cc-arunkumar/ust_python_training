import csv
data=[]
with open("employee_data01.csv","r") as file:
    csv_reader=csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        data.append(row)

with open("filtered_data.csv","w",newline='')as file:
    csv_writer=csv.writer(file)

    for i in data:
        salary=float(i[3])
        if(salary>60000):
            csv_writer.writerow(i)