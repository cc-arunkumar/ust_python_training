import csv
with open("employee_dict_file.csv",mode='r')as file:
    csv_dict_reader=csv.reader(file)
    for row in csv_dict_reader:
        print(row)
        
        
# ['id', 'name', 'dept', 'sal']
# ['201', 'suresh', 'Sales', '58000']
# ['202', 'Meena', 'IT', '72000']
# ['203', 'Amit', 'HR', '64000']