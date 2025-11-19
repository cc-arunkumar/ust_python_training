
import csv
from typing import List,Dict

def read_csv(path: str) -> List[Dict[str, str]]:
    print("---> ",path)
    with open(path,'r', newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            return row

def write_csv(path: str, rows: List[Dict[str, str]], headers: List[str]) -> None:
    with open(path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
        

# import csv

# def read_csv(path: str) -> list[dict[str, str]]:
#     with open(path, newline="") as file:
#         reader = csv.DictReader(file)
#         return list(reader)   


