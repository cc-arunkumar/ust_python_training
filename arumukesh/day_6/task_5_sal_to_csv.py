import csv

# the program prints the details of the employees having salary more than 60000

with open("employee_data01.csv","r")as file:
    reader=csv.reader(file)
    next(reader)
    # opening writable csv to write the values
    with open("higher_sal.csv","w",newline='') as file01:
        writer=csv.writer(file01)
        for row in reader:
            
            id,name,department,salary=row
            salary=float(salary)
            # checks the salry and writes to higher_sal.csv
            if salary>60000:
                writer.writerow(row)
