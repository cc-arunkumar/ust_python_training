import csv

data_path = r"C:\Training\Day6\employee_data01.csv"
count = 0
list = []

with open(data_path, 'r') as file:
    csv_reader = csv.reader(file)
    
# Remove header from CSV File
    next(csv_reader)
# employees salary more than 60000
    for row in csv_reader:
        if int(row[3])>60000:
            print(row)
 # number of employees in IT
        if row[2] == "IT":
            count += 1
print("tot num of IT employees:",count)

#write filtered data into new file high_salary.csv

data = [
    ["id", "name", "department", "salary"],
    [101, "Arun", "IT", 70000],
    [102, "Riya", "HR", 65000],
    [103, "John", "Finance", 60000],
    [104, "Neha", "Marketing", 55000]
]

with open("employee_data02.csv",mode="w",newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
print("==csv file created===")

# sample output:
# ['202', 'Meena', 'IT', '72000']
# ['203', 'Amit', 'HR', '64000']
# tot num of IT employees: 1
# ==csv file created===



            


    