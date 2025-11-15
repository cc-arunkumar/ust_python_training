#Read and write in csv

import csv

#Dummy data
data=[
    {"emp_id":101,"name":"Arjun","designation":"IT","salary":10000},
    {"emp_id":102,"name":"Arun","designation":"IT","salary":12000},
    {"emp_id":103,"name":"Akhil","designation":"IT","salary":13000},
]

#Open file in write mode
with open("D:/ust_python_training-1/arjun_j_s/day_10/data/emp_details.csv","w",newline="") as file:
    header=["emp_id","name","designation","salary"]
    csv_file = csv.DictWriter(file,header)
    csv_file.writeheader()
    csv_file.writerows(data)

#Open file in read mode
with open("D:/ust_python_training-1/arjun_j_s/day_10/data/emp_details.csv","r") as file:
    csv_file = csv.DictReader(file)
    for data in csv_file:
        print(data)
        
#Output
# {'emp_id': '101', 'name': 'Arjun', 'designation': 'IT', 'salary': '10000'}
# {'emp_id': '102', 'name': 'Arun', 'designation': 'IT', 'salary': '12000'} 
# {'emp_id': '103', 'name': 'Akhil', 'designation': 'IT', 'salary': '13000'}