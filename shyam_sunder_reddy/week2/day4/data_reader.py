import csv
with open("data/emp_details.csv","r") as file:
    
    #gives the raw data
    # filereader=csv.reader(file)
    # next(filereader)
    # for row in filereader:
    #     print(row)
    
    #gives data in key,value pairs    
    filedictreader=csv.DictReader(file)
    for value in filedictreader:
        print(value)