import csv

def read_csv(path):
    with open(path,"r") as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data

def write_csv(path,data,headers):
    with open(path,"w",newline="") as file:
        writer = csv.DictWriter(file,headers)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

