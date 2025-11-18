import csv 
def read_csv(targetpath):
    with open(targetpath,"r") as file:
        content=csv.DictReader(file)
        return list(content)
        
def write_csv(targetpath,listdict,headers):
    with open(targetpath,"w",newline='') as file:
        content=csv.DictWriter(file,fieldnames=headers)
        content.writeheader()
        for row in listdict:
            content.writerow(row)
        
    

        