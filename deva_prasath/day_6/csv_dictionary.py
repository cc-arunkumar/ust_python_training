import csv
#Data to write
employees=[
    {"id" :201,"name":"Deva","department":"Sales","salary":560000},
    {"id": 202,"name":"Raj","department":"IT","salary":70000},
    {"id": 203,"name":"Vikaram","department":"HR","salary":65000}
]
#Create a CSV file in write mode
with open('employee_dict_data.csv',mode='w',newline='') as file:
    #create dictionary object
    header=["id","name","department","salary"]
    
    writer=csv.DictWriter(file,fieldnames=header)
    #to print the header names
    writer.writeheader()
    #write employee data to csv file
    writer.writerows(employees)
    
print("====CSV Writing Dictionary Completed====")

#Reading CSV file using dictreader
with open('employee_dict_data.csv',mode='r') as file:
    csv_dict_reader=csv.DictReader(file)
    for row in csv_dict_reader:
        print(row)


#Sample output
#all in dictionary

# {'id': '201', 'name': 'Deva', 'department': 'Sales', 'salary': '560000'}
# {'id': '202', 'name': 'Raj', 'department': 'IT', 'salary': '70000'}
# {'id': '203', 'name': 'Vikaram', 'department': 'HR', 'salary': '65000'}