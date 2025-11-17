import csv
from typing import List, Dict


def read_csv(path: str) -> List[Dict[str, str]]:
    """Read a CSV file and return a list of dicts (field -> value)."""
    rows: List[Dict[str, str]] = []
    with open(path, mode="r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # DictReader returns OrderedDict[str, str | None]; we keep as dict[str, str]
            clean_row: Dict[str, str] = {k: (v if v is not None else "") for k, v in row.items()}
            rows.append(clean_row)
    return rows


def write_csv(path: str, rows: List[Dict[str, str]], headers: List[str]) -> None:
    """Overwrite the CSV file with given headers and rows."""
    with open(path, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
