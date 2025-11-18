import csv
import os

current = "C:/Users/Administrator/Desktop/ust_python_training/akhil_praveen/day12/task-package-module/data"

def read_csv(filename):
    with open(current+filename,"r") as file:
        csv_file = csv.DictReader(file)
        header = csv_file.fieldnames
    return csv_file,header        