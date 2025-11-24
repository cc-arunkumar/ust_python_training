import csv
from typing import List, Dict, Any

def read_csv(path: str) -> List[Dict[str, Any]]:
    """
    Reads a CSV file and returns a list of dictionaries, one per row.

    Args:
        path (str): Path to the CSV file.

    Returns:
        List[Dict[str, Any]]: List of rows as dictionaries.
    """
    with open(path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data


def write_csv(path: str, data: List[Dict[str, Any]], headers: List[str]) -> None:
    """
    Writes a list of dictionaries to a CSV file.

    Args:
        path (str): Path to the CSV file to write.
        data (List[Dict[str, Any]]): List of dictionaries to write as rows.
        headers (List[str]): List of column headers for the CSV.

    Returns:
        None
    """
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for item in data:
            writer.writerow(item)
