#Task 3:
#Write the filtered data (salary > 60000) into a new file high_salary.csv.

import csv


with open("employee_data01.csv","r") as file:
    with open("high_salary.csv","w",newline="") as new_file:
        cs_data=d=csv.reader(file)
        next(cs_data)
        new_csv = csv.writer(new_file)
        for data in cs_data:
            if(int(data[3])>60000):
                new_csv.writerow(data)
#Output
#Data in new csv :
# 101 Arun IT 70000
# 102 Riya HR 65000