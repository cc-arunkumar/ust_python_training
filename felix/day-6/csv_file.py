# CSV file 

import csv

# reading csv file
with open("example.csv","r") as file:
    csv_reader = csv.reader(file)
    
    
    # remove first row
    next(csv_reader)
    
    for row in csv_reader:
        print(row)
        
# writing in csv file

