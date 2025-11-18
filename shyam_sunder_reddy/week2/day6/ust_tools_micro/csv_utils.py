import csv

def read_csv(path):
    data=[]
    with open (path,"r") as file:
        reader=csv.DictReader(file)
        for key in reader:
            data.append(key)
    return data
    
def write_csv(data):
    for row in data:
        print(row)