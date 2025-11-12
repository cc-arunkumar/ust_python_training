import csv

# Reading csv file
with open('employee_data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    
    # Skip header
    next(csv_reader, None)
    
    # Initialize counter
    it_count = 0
    
    for row in csv_reader:
        department = row[2].strip().lower()  # Assuming department is in the 3rd column (index 2)
        if department == 'it':
            it_count += 1
    
    print(f"Number of employees in IT department: {it_count}")
