
import csv


def read_csv(path: str) -> list[dict[str, str]]:
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]            
            

def write_csv(path: str, rows: list[dict[str, str]], headers: list[str]) -> None:
    
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
