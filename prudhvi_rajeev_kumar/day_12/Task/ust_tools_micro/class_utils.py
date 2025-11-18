import csv

def read_csv(path : str) -> list[dict[str, str]]:
    with open(path, mode = 'r', newline='') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]
    
def write_csv(path: str, rows: list[dict[str, str]], headers: list[str]) -> None:
    with open(path, mode= 'w', newline='', encoding='utf-8') as file:
        if not rows:
            return
        
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writerows(rows)
        

        
        