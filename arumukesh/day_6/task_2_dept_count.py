import csv
dept_count={}
with open("employee_data01.csv","r")as file:
    csv_reader=csv.reader(file)
    next(csv_reader)
    c=0
# creating summary vals according to the data agiven
    for rows in  csv_reader:
        id,name,department,salary=rows
        if department not in dept_count:
            dept_count[department]=1
        if department in dept_count:
            dept_count[department]+=1
        

    for dept,count in dept_count.items():
        print(dept,count)



        

        