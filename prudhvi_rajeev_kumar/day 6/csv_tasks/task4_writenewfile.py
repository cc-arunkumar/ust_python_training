import csv 

#The task was to find the employees with salary greater than 60k and write them in another file
with open('employeedata01.csv', 'r') as file:
    #step 1 : Read the file 
    csv_reader = csv.reader(file)
    header = next(csv_reader) 
    #step 2 : Opening a new file and writing the values that we got
    with open('high_salary.csv', 'w', newline='') as newfile:
        csv_writer = csv.writer(newfile)
        csv_writer.writerow(header)  
        #Step 3 : Iterating over the rows of old files and writing them in new file
        for row in csv_reader:
            if int(row[3]) > 60000: 
                csv_writer.writerow(row)  
                print(row)  


            
