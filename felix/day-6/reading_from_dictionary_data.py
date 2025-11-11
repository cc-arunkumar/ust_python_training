# Reading from dictionary data

import csv

#step 1 : create or open csv file in write mode
with open("employee_dict_data.csv","r") as file2:
    
    # step 3 : create dictwriter object
    reader = csv.DictReader(file2)
    
    for row in reader:
        print(row)