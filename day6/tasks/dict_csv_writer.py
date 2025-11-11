import csv
employees=[
    {"id":201,"name":"suresh","dept":"Sales","sal":58000},
    {"id":202,"name":"Meena","dept":"IT","sal":72000},
    {"id":203,"name":"Amit","dept":"HR","sal":64000} ]

with open('employee_dict_file.csv',mode='w',newline='')as file:
    header=["id","name","dept","sal"]
    # creating a dictwritter object
    writer=csv.DictWriter(file,fieldnames=header)
    # creating the header to the csv file
    writer.writeheader()
    # write employee data to csv file 
    writer.writerows(employees)