import os
import csv

def read_csv(path):

    with open(path,"r") as file:
        
        file_data = csv.DictReader(file)
        header = file_data.fieldnames
        return list(file_data)

def write_csv(path,rows,header):

    with open(path,"w",newline="") as file:
        file_data = csv.DictWriter(file,header)
        file_data.writeheader()
        file_data.writerows(rows)

