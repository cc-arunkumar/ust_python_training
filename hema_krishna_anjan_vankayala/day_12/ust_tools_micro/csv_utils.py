import csv
def read_csv(path):
    li=[]
    with open(path,'r') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            li.append(row)
    return li 

def write_csv(path,li,headers):
    with open(path,'w',newline='') as f:
        writer = csv.DictWriter(f,fieldnames=headers)
        writer.writeheader()
        writer.writerows(li)
    