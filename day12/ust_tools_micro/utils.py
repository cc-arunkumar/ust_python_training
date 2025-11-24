import csv
from typing import List, Dict


def read_csv(path: str)->List[Dict[str, str]]:
    with open(path,mode='r',newline='') as file:
        reader=csv.DictReader(file)
        return[row for row in reader]
    
    
def write_csv(path: str, rows: List[Dict[str, str]], headers: List[str])-> None:
    with open(path,mode='w',newline='') as file:
        writer=csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)