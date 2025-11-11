import csv
count=0
with open("employee_data01.csv",mode="r") as file:
    csv_reader=csv.reader(file)
    for id,name,department,salary in csv_reader:
        if department=="IT":
            count+=1
            print(f"number of IT members={count}")
            
#  øutput           
# number of IT members=1