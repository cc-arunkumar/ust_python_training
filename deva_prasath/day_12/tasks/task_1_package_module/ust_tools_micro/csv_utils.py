import csv
def read_csv(path):
    #creating a list
    orders=[]
    with open(path,'r') as file:
        #dictreader
        reader=csv.DictReader(file)
        for row in reader:
            #appending the lines
            orders.append(row)
    return orders

def write_csv(path,orders,headers):
    with open(path,'w',newline=' ') as f:
        writer=csv.DictWriter(f,fieldnames=headers)
        writer.writeheader()
        for row in orders:
            writer.writerow(row)
            

