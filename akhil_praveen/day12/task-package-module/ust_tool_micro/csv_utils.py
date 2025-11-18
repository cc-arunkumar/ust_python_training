import csv
import os


def read_csv(path):
    with open(path,"r") as file:
        csv_file = csv.DictReader(file)
        header = csv_file.fieldnames
        return list(csv_file),header        