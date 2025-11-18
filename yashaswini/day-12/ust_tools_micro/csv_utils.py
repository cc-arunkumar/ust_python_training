import csv

def read_csv(path: str):
    """Read a CSV file and return a list of dictionaries."""
    rows = []
    with open(path, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows

def write_csv(path: str, rows, headers):
    """Write rows (list of dicts) into a CSV file with given headers."""
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
