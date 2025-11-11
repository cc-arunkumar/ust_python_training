# Writing filtered data into new file

import csv


with open("employee_data.csv","r") as file:
    csv_reader = csv.reader(file)
    
    
    # remove first row
    next(csv_reader)
    
    print("Employees whose salary greater than 60000: ")
    
    # iterating through each row of data
    for row in csv_reader:
        if int(row[3])>60000:
            with open("sorted_data.csv",mode="a",newline="") as file1:
                csv_writer = csv.writer(file1)
                csv_writer.writerows([row])
                print(row[1])
                
    print("Data stored in file")
                
# output

# Employees whose salary greater than 60000: 
# Arun
# Riya
# Data stored in file