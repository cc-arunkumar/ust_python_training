import csv

with open("data/emp_details.csv","w") as file:
    write = csv.writer(file)
    write.writerow(['101', 'Felix', 'IT', '50000'])
    write.writerow(['102', 'Arun', 'HR', '60000'])
    write.writerow(['103', 'Akhil', 'IT', '70000'])
    write.writerow(['101', 'Felix', 'IT', '50000'])
    
with open("data/emp_details.csv","r") as file:
    reader = csv.reader(file)
    for data in reader:
        print(data)