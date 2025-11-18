import csv

def read_csv(path: str):
    """Read a CSV file and return a list of dictionaries."""
    rows = []

    # Open the CSV file in read mode
    with open(path, "r", newline="") as f:
        # DictReader converts each row into a dictionary
        reader = csv.DictReader(f)

        # Loop through each row and store it in a list
        for row in reader:
            rows.append(row)

    # Return the complete list of row dictionaries
    return rows


def write_csv(path: str, rows, headers):
    """Write rows (list of dicts) into a CSV file with given headers."""

    # Open the CSV file in write mode
    with open(path, "w", newline="") as f:
        # DictWriter uses headers as column names
        writer = csv.DictWriter(f, fieldnames=headers)

        # Write the header row first
        writer.writeheader()

        # Write each dictionary as one CSV row
        for row in rows:
            writer.writerow(row)
