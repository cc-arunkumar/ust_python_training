# csv_utils.py

import csv

def read_csv(path: str) -> list[dict[str, str]]:
    """Read CSV file and return list of row dictionaries."""
    with open(path, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def write_csv(path: str, rows: list[dict[str, str]], headers: list[str]) -> None:
    """Write rows into CSV file with the given headers."""
    with open(path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

