# csv_utils.py

import csv

# Global list that will store rows read from any CSV file.

new_list = []

def read_csv_file(path):

    # Read a CSV file and return a list of dictionaries,
    # where each dictionary represents a row.

    with open(path, "r") as file:
        csv_reader = csv.DictReader(file)

        # Loop through all rows and store them in new_list
        for row in csv_reader:
            new_list.append(row)

    return new_list


def write_csv_file(path, rows, headers):
    
    # Write a list of dictionaries to a CSV file with the specified headers.
    
    with open(path, "w") as f:
        # Create a DictWriter using the header fieldnames
        csv_writer = csv.DictWriter(f, fieldnames=headers)

        # Write the header row
        csv_writer.writeheader()

        # Write multiple row dictionaries
        csv_writer.writerows(rows)
