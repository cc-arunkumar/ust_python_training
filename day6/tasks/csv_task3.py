import csv

# Read from the original file
with open("employee_data01.csv", 'r') as file:
    csv_reader = csv.reader(file)

    # Convert reader to a list to safely
    rows = list(csv_reader)

    if rows:  # Check if there at least one row
        header = rows[0]  # First row is header

        # Write to a new file
        with open("employee_data.csv", mode='w', newline='') as file1:
            csv_writer = csv.writer(file1)
            csv_writer.writerow(header)

            for row in rows[1:]:  # Skip header
                id, name, dept, sal = row
                sal = float(sal)
                if sal > 60000:
                    csv_writer.writerow([id, name, dept, sal])
