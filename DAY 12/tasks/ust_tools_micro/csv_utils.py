import csv

# Read CSV file and return list of dictionaries
def read_csv(path):
    with open(path, "r", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

# Write rows (list of dicts) to CSV file with given headers
def write_csv(path, rows, headers):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()  # Write header row
        writer.writerows(rows)  # Write all data rows