#CSV Dict Reading


import csv
with open('employee_dict_data.csv',mode='r') as file:
    csv_dict_reader=csv.DictReader(file)
    for row in csv_dict_reader:
        print(row)
        
print("CSV Reading complete")



#output
# {'id': '401', 'name': 'varsha', 'department': 'Development', 'salary': '800000'}
# {'id': '402', 'name': 'yashu', 'department': 'Development', 'salary': '900000'}
# {'id': '404', 'name': 'bhargavi', 'department': 'Testing', 'salary': '1800000'}
# {'id': '406', 'name': 'vinutha', 'department': 'support', 'salary': '100000'}  
# CSV Reading complete