import csv 
from typing import List,Dict

# def read_csv(path : str) -> List[dict[str,str]]:
#     with open("order.csv", "r",newline="") as file:
#         reader = csv.DictReader(file)
#         list=[]
#         for row in reader:
#             list.append(row)
        
    
#     with open("inventory.csv","r",newline="") as outfile:
#         csv_reader=csv.DictReader(outfile)
#         list2=[]
#         for row in csv_reader:
#             list2.append(row)
#         return list2
    
# def write_csv(path: str, rows: List[Dict[str, str]], headers: List[str]) -> None:
#     with open("order.csv","w",newline=headers) as outfile:
#         writer = csv.DictWriter(outfile, fieldnames=headers)
#         writer.writeheader()
#         writer.writerows(rows)
#     with open("inventory.csv","w",newline=headers) as infile:
#         writer=csv.DictWriter(infile,fieldnames=headers)

def read_csv(path: str) -> List[Dict[str, str]]:
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

def write_csv(path: str, rows: List[Dict[str, str]], headers: List[str]) -> None:
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

        
        
    