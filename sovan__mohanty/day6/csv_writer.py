
import csv
#Data to write
employees=[{"id":201,"name":"Suresh","department":"Sales","salary":58000},
           {"id":202,"name":"Suraj","department":"Sales","salary":56000},
           {"id":202,"name":"Suman","department":"Sales","salary":59000}]
#Step 1 create or open a CSV file in write mode
# with open('employee_dict_data.csv','w',newline='') as file:
    
#     #Step2: Create the filenmes (header)
#     header=['id','name','department','salary']
    
#     #Step 3: Create a Dictwriter object
#     writer=csv.DictWriter(file,fieldnames=header)
    
#     #Step 4: Write the header to the CSV file
    
#     writer.writeheader()
    
#     #Step 5: Write the employee data to the CSV file
#     writer.writerows(employees)
    
    #print("=== CSV Writing With Dictionary Completed ===")
#Step 1 open employee_dict_data csv file in read mode
with open('employee_dict_data.csv','r',newline='') as file:
    #Step 2: create a DictReader object
    csv_reader=csv.DictReader(file)
    
    #Step 3: print the csv row by row
    for row in csv_reader:
        print(row)