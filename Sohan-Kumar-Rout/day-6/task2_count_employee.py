#Task 2: Count how many employee belong to IT dept
import csv
count=0
with open("employee_data.csv","r") as file:
    csv_reader=csv.DictReader(file)
    
    for row in csv_reader:
        if(row['department']=="IT"):
            count+=1
            print("Number of employee belong to IT department ",count)
            
#Output
# Number of employee belong to IT department  1