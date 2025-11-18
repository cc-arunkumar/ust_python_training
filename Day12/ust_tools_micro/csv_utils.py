# ust_tools_micro/csv_utils.py
import csv

path = "Day12\\data\\orders.csv"

def read_csv(path):
    rows = []
    with open(path,"r") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            rows.append(row)
    return rows

def write_csv(path, rows, headers):
    with open(path, "w") as fh:
        writer = csv.DictWriter(fh, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
