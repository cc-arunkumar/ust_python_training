#Task 3 : Write the filtered data salary greater than 60000 into a new file
import csv 
with open("employee_data.csv", "r", newline='') as file, open('high_salary.csv',"w",newline='') as outfile:
    reader = csv.DictReader(file)
    fieldnames= reader.fieldnames
    writer= csv.DictWriter(outfile,fieldnames=fieldnames)
    writer.writeheader()
    #File reading using for loop
    for row in reader:
        if int(row['salary'])>60000:
            writer.writerow(row)
            