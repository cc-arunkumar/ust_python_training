#CSV Dictionary file
# reading the dictionary csv file
import csv   # Import the CSV module to handle CSV file operations

# Open the CSV file in read mode
with open('employee_dict_data.csv', mode='r') as file:
    # Create a DictReader object which reads each row into a dictionary
    # Keys are taken from the first row (header) of the CSV file
    csv_dict_reader = csv.DictReader(file)

    # Iterate through each row in the CSV file
    for row in csv_dict_reader:
        # Each row is a dictionary: {column_name: value}
        print(row)

    
# Sample Output
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day6> & "C:/Program Files/Python314/python3.14t.exe" c:/Users/Administrator/Desktop/Training/ust_python_training/vinutha/day6/csv_reader_dict.py
# {'id': '401', 'name': 'hima', 'department': 'Development', 'salary': '800000'}
# {'id': '402', 'name': 'chakitha', 'department': 'Development', 'salary': '900000'}
# {'id': '404', 'name': 'siri', 'department': 'Testing', 'salary': '1800000'}       
# {'id': '406', 'name': 'vinnu', 'department': 'support', 'salary': '100000'}       
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day6> 