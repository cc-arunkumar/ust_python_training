#CSV Dictionary file
# reading the dictionary csv file
import csv

with open('employee_dict_data.csv',mode='r') as file:
    csv_dict_reader=csv.DictReader(file)
    for row in csv_dict_reader:
        print(row)
    
# Sample Output
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day6> & "C:/Program Files/Python314/python3.14t.exe" c:/Users/Administrator/Desktop/Training/ust_python_training/vinutha/day6/csv_reader_dict.py
# {'id': '401', 'name': 'hima', 'department': 'Development', 'salary': '800000'}
# {'id': '402', 'name': 'chakitha', 'department': 'Development', 'salary': '900000'}
# {'id': '404', 'name': 'siri', 'department': 'Testing', 'salary': '1800000'}       
# {'id': '406', 'name': 'vinnu', 'department': 'support', 'salary': '100000'}       
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day6> 