import csv
from typing import List, Dict

def read_csv(path: str) -> List[Dict[str, str]]:
    with open(path, mode="r", newline="") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]


def write_csv(path: str, rows: List[Dict[str, str]], headers: List[str]) -> None:
    with open(path, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
