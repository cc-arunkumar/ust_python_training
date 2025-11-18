import csv

# Function to read a CSV file and return the data as a list of dictionaries
def csv_reader(path):
    order = []  
    with open(path, "r") as file:  
        csv_read = csv.DictReader(file)  
        for row in csv_read:  
            order.append(row)  
    return order  # Return the list of rows as dictionaries

# Function to write data to a new CSV file
def write_csv(path1, order, header):
    with open(path1, "w", newline="") as file1:  # Open the file in write mode, clearing any existing content
        csv_writer = csv.DictWriter(file1, fieldnames=header) 
        csv_writer.writeheader()  
        for row in order:  
            csv_writer.writerow(row)  # Write each dictionary as a row in the CSV file
