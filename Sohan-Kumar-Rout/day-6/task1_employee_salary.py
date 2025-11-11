#Task :1 find employee whose sal is greater than 600000

with open("employee_data.csv","r") as file:
    csv_reader= csv.DictReader(file)
    # next(csv_reader)
    
    for row in csv_reader:
        if(float(row['salary'])>60000):
            print("Employee whose salary is more than 60000 : ",row['name'])
#output
# Arun
# Riya
